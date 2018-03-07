import socket
import sys
import getopt
import logging
import pickle

logging.basicConfig(format='%(asctime)s %(message)s')
logger = logging.getLogger('')
            
buffer_size = 4096

def main(argv):
    port = 10000
    client_port = 10001

    try:
        opts, args = getopt.getopt(argv,"hp:",["port=", "log="])
    except getopt.GetoptError:
        print('server.py -p <port> --log=<debug|...>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('server.py -p <port> --log=<debug|...>')
            sys.exit()
        elif opt in ("-p", "--port"):
            port = int(arg)
        elif opt in ("--log"):
            numeric_level = getattr(logging, arg.upper(), None)
            if not isinstance(numeric_level, int):
                raise ValueError('Invalid log level: %s' % arg)
            logger.setLevel(numeric_level)                        

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(('localhost', port))

    while True:
        logger.debug('Waiting to receive message')
        data, address = sock.recvfrom(buffer_size)
    
        logger.debug('Received {} bytes from {}'.format(len(data), address))
    
        if data:
            info = pickle.loads(data)
            logger.info('Received: {}'.format(info))
            client_address = (address[0], info[2])
            sent = client_sock.sendto(data, client_address)
            logger.debug('Sent {} bytes back to {}'.format(sent, client_address))

if __name__ == "__main__":
    main(sys.argv[1:])
