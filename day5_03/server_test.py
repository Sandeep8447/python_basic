# -*- coding:utf-8 -*-
__auth__ = 'christian'
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_port = ('127.0.0.1', 8080)
sock.bind(ip_port)
sock.listen(5)

while True:
    connection, address = sock.accept()
    #connection.send("HTTP/1.1 200 OK\r\n\r\n")
    connection.send('hello.')
    flag = True
    while flag:
        data = connection.recv(1024)  # data interactive
        print data
        if data == 'exit':
            flag = False
        connection.send('sb')
    connection.close()