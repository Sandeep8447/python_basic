# -*- coding:utf-8 -*-
__auth__ = 'christian'

import os
import socket
import threading
import SocketServer

SERVER_HOST = 'localhost'
SERVER_PORT = 0  # tell the kernel to pick up a port dynamically
BUF_SIZE = 1024
ECHO_MSG = 'Hello echo server!'

class ForkingClient():
    """A client to test forking server."""
    def __init__(self, ip, port):
        # create a socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the server
        self.sock.connect((ip, port))

    def run(self):
        """Client playing with the server"""
        # Send the data to server
        current_process_id = os.getpid()
        print 'PID %s Sending echo message to the server : "%s"' % (current_process_id, ECHO_MSG)
        send_data_length = self.sock.send(ECHO_MSG)
        print "Sent: %d characters, so far..." % send_data_length

        # Display server response
        response = self.sock.recv(BUF_SIZE)
        print "PID %s Received: %s" % (current_process_id, response[5:])

    def shutdown(self):
        """Cleanup the client socket"""
        self.sock.close()
