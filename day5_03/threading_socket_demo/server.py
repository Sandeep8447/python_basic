# -*- coding:utf-8 -*-
__auth__ = 'christian'

import SocketServer

class MyServer(SocketServer.BaseRequestHandler):  #inheritance

    def setup(self):
        pass

    def handle(self):
        # print self.request
        # print self.client_address
        # print self.server
        connection = self.request
        connection.send('hello.')
        flag = True
        while flag:
            data = connection.recv(1024)  # data interactive
            print data
            if data == 'exit':
                flag = False
            connection.send('sb')
        connection.close()

    def finish(self):
        pass


if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1', 8090), MyServer)  # init
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

    TCPServer                   ThreadingMixIn:
        --:__ini__
            BaseServer.__init__(self, server_address, RequestHandlerClass)  # classic class constructor not super()

    ThreadingTCPServer

    '''
    server.serve_forever()