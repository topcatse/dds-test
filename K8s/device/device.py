import socket
import sys
import getopt
import time
import logging
import pickle

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
logger = logging.getLogger('')
logger.setLevel(logging.INFO)

buffer_size = 4096

def main(argv):
    count = 1
    port = 10001
    server_address = 'localhost'
    server_port = 10000
    sleep_s = 1
    id = 0
    
    try:
        opts, args = getopt.getopt(argv,"hc:p:a:s:i:",["count=", "port=", "serveraddress=", "serverport=", "id=", "sleep=", "log="])
    except getopt.GetoptError:
        print('device.py -c <count> -p <port> -a <serveraddress> -s <serverport> --id=<id> --sleep=<secs> --log=<debug|...>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('device.py -c <count> -p <port> -a <serveraddress> -s <serverport> --id=<id> --sleep=<secs> --log=<debug|...>')
            sys.exit()
        elif opt in ("-c", "--count"):
            count = int(arg)
        elif opt in ("-p", "--port"):
            port = int(arg)
        elif opt in ("-a", "--serveraddress"):
            server_address = arg
        elif opt in ("-s", "--serverport"):
            server_port = int(arg)
        elif opt in ("-i", "--id"):
            id = int(arg)
        elif opt in ("--sleep"):
            sleep_s = int(arg)
        elif opt in ("--log"):
            numeric_level = getattr(logging, arg.upper(), None)
            if not isinstance(numeric_level, int):
                raise ValueError('Invalid log level: %s' % arg)
            logger.setLevel(level=numeric_level)            

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(('localhost', port))

    info = [id, 0, port]
    
    try:    
        for c in list(range(count)):
            info[1] = c
            logger.info('Sending {}'.format(info))
            sent = server_sock.sendto(pickle.dumps(info), (server_address, server_port))

            logger.debug('Waiting to receive')
            data, server = sock.recvfrom(buffer_size)
            logger.debug('Received {} bytes from {}'.format(len(data), server))

            if data:
                logger.info('Received: {}'.format(pickle.loads(data)))

            time.sleep(sleep_s)

    finally:
        logger.debug('Closing sockets')
        server_sock.close()
        sock.close()    

if __name__ == "__main__":
    main(sys.argv[1:])
