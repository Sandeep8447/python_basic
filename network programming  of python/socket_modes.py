#!/usr/bin/env python
# Python Network Programming Cookbook
# This program is optimized for Python 2.7. It may run on any
# other Python version with/without modifications.

# socket modes: blocking and non-blocking
# 1 set blocking
# 0 set non-blocking

import  socket

def test_socket_modes():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(1)
    s.settimeout(0.5)
    s.bind(("127.0.0.1", 0))

    socket_address = s.getsockname()
    print "Trivial Server launch on socket: %s" %str(socket_address)
    while 1:
        s.listen(1)  # still listening

if __name__ == '__main__':
    test_socket_modes()