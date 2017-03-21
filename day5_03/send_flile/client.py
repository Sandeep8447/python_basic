# -*- coding:utf-8 -*-
__auth__ = 'christian'

import socket
import os
import sys

ip_port = ('127.0.0.1', 9999)
sock = socket.socket()
sock.connect(ip_port)

container = {'key': '', 'data': ''}

while True:
    input = raw_input('path:')
    cmd, path = input.split('|')
    fileName = os.path.basename(path)
    fileSize = os.stat(path).st_size
    sock.send(cmd + "|" + fileName + "|" + str(fileSize))
    sendSize = 0
    f = file(path, 'rb')
    Flag = True
    while Flag:
        if sendSize + 1024 > fileSize:
            data = f.read(fileSize - sendSize)
            Flag = False
        else:
            data = f.read(1024)
            sendSize += 1024
        sock.send(data)
    f.close()
    sock.close()