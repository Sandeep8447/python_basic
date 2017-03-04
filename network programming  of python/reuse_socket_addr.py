# -*-coding:utf-8-*-
#!/usr/bin/env python
# Python Network Programming Cookbook
# This program is optimized for Python 2.7. It may run on amy
# other Python version with/without modifications.



'''
运行在某个端口上的一个python套接字服务器，连接一次之后便终止运行，就不能在使用这个端口了。
这个问题的解决方式就是启用套接字重用选项SO_REUSEADDR
'''

import socket
import sys

def reuse_socket_addr():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the old state of the 'SO_REUSEADDR' option
    old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print "Old sock state: %s" %old_state

    # Enable the 'SO_REUSEADDR' option
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    new_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print "New sock state: %s" %new_state

    local_port = 8080

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # commented code
    srv.bind(('127.0.0.1', local_port))
    srv.listen(1)
    print ('Listening on port: %s' %local_port)
    while True:
        try:
            connection, addr = srv.accept()
            print 'Connected by %s:%s' % (addr[0], addr[1])
        except KeyboardInterrupt:
            break
        except socket.error, msg:
            print '%s' % (msg,)

if __name__ == '__main__':
    reuse_socket_addr()