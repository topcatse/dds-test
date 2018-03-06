import socket
import sys
import getopt

buffer_size = 4096

def main(argv):
    count = 1
    port = 10001
    server_address = 'localhost'
    server_port = 10000
    
    try:
        opts, args = getopt.getopt(argv,"hc:p:a:s:",["count=", "port=", "serveraddress=", "serverport="])
    except getopt.GetoptError:
        print('client.py -c <count> -p <port> -a <serveraddress> -s <serverport>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('client.py -c <count> -p <port> -a <serveraddress> -s <serverport>')
            sys.exit()
        elif opt in ("-c", "--count"):
            count = int(arg)
        elif opt in ("-p", "--port"):
            port = arg
        elif opt in ("-a", "--serveraddress"):
            server_address = arg
        elif opt in ("-s", "--serverport"):
            server_port = arg

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(('localhost', port))

    try:    
        for c in list(range(count)):
            message =  'This is message {}'.format(c)
            print('Sending "{}"'.format(message))
            sent = server_sock.sendto(message.encode(), (server_address, server_port))

            print('waiting to receive')
            data, server = sock.recvfrom(buffer_size)
            print('Received {} bytes from {}'.format(len(data), server))

            if data:
                print('With content: "{}"'.format(data.decode()))

    finally:
        print('Closing sockets')
        server_sock.close()
        sock.close()    

if __name__ == "__main__":
    main(sys.argv[1:])
