#!/usr/bin/env python
# Python Network Programming Cookbook
# This program is optimized for Python 2.7. It may run on amy
# other Python version with/without modifications.

import socket

def convert_integer():
    data = 1234
    # 32-bit
    print "Original: %s => Long host byte order: %s, Network byte order: %s" % \
          (data, socket.ntohl(data), socket.htonl(data))
    # 17-bit
    print "Original: %s => Short host byte order: %s, Network byte order: %s" % \
          (data, socket.ntohs(data), socket.htons(data))

if __name__ == '__main__':
    convert_integer()