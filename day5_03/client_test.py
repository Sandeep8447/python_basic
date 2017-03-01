# -*- coding:utf-8 -*-
__auth__ = 'christian'

import socket

ip_port = ('127.0.0.1', 8080)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ip_port)

while True:
    data = client.recv(1024)
    print data
    inp = raw_input('client: ')
    client.send(inp)
    if inp == 'exit':
        break