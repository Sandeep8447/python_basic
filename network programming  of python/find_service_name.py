#!/usr/bin/env python
# Python Network Programming Cookbook
# This program is optimized for Python 2.7. It may run on amy
# other Python version with/without modifications.

import socket

def find_service_name():
    protocol_name = 'tcp'
    for port in [80, 25, 3306, 22, 21]:
        print 'Port: %s => service name: %s' %(port, socket.getservbyport(port, protocol_name))
    print 'Port: %s => service name: %s' % (53, socket.getservbyport(53, 'udp'))

if __name__ == '__main__':
    find_service_name()