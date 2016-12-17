# -*- coding:utf-8 -*-
__auth__ = 'christian'

import SocketServer

class MyServer(SocketServer.BaseRequestHandler):  #inheritance

    def handle(self):
        print self.request, self.client_address, self.server


if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)  # init
    '''
    class ThreadingTCPServer(ThreadingMixIn, TCPServer): pass

    server.server_address = ('127.0.0.1', 9999)
    server.RequestHandlerClass = MyServer
    '''

    '''
    BaseServer
        --:__ini__
            server.server_address = ('127.0.0.1', 9999)
            server.RequestHandlerClass = MyServer

    TCPServer                   ThreadingMixIn
        --:__ini__
            BaseServer.__init__(self, server_address, RequestHandlerClass)  # classic class constructor not super()

    ThreadingTCPServer

    '''
    server.serve_forever()