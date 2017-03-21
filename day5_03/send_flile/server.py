# -*- coding:utf-8 -*-
__auth__ = 'christian'

import SocketServer
import os

class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        basePath = 'F:/Tmp'
        conn = self.request
        print "connected..."
        while True:
            pre_data = conn.recv(1024)
            cmd, fileName, fileSize = pre_data.split('|')
            recvSize = 0
            fileDir = os.path.join(basePath,fileName)
            f = file(fileDir, 'wb')
            Flag = True
            while Flag:
                if int(fileSize) > recvSize:
                    data = conn.recv(1024)
                    recvSize += len(data)
                else:
                    recvSize = 0
                    Flag = False
                f.write(data)
            print "Update successed..."
            f.close()

instance = SocketServer.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
instance.serve_forever()