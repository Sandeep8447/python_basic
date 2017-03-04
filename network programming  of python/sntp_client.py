# -*-coding:utf-8-*-
#!/usr/bin/env python
# Python Network Programming Cookbook
# This program is optimized for Python 2.7. It may run on amy
# other Python version with/without modifications.

import socket
import struct
import sys
import time

NTP_SERVER = "0.uk.pool.ntp.org"
TIME1970 = 2208988800L

def sntp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data = '\x1b' + 47 * '\0'
    client.sendto(data, (NTP_SERVER, 123))
    data, address = client.recvfrom(1024)
    if data:
        print 'Response received from:', address
    t = struct.unpack('!12I', data)[10]
    t -= TIME1970
    print '\tTime=%s' % time.ctime(t)

if __name__ == '__main__':
    sntp_client()