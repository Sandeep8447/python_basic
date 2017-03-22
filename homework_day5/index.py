# -*- coding:utf-8 -*-
__auth__ = 'christian'

import os
import socket
import threading
from utility.server import ThreadedTCPServer, ThreadedTCPRequestHandler
from utility.client import ForkingClient

SERVER_HOST = 'localhost'
SERVER_PORT = 0  # tells the kernel to pickup a port dynamically
BUF_SIZE = 1024

def main():
    # Run Server
    server = ThreadedTCPServer((SERVER_HOST, SERVER_PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address  # retrieve ip address

    # Start a thread with the server -- one thread per request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread exits
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running on thread: %s" % server_thread.name

    # Launch the client
    client1 = ForkingClient(ip, port)
    client1.run()

    client2 = ForkingClient(ip, port)
    client2.run()

    # Clean them up
    server.shutdown()
    client1.shutdown()
    client2.shutdown()
    #server.socket.close()
    server.shutdown()

if __name__ == '__main__':
    main()

