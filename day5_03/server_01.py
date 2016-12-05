# -*- coding:utf-8 -*-
__auth__ = 'christian'

import socket  # something wrong.

# handle the client request
def handle_request(client):
    buf = client.recv(1024)
    #client.send("HTTP/1.1 200 OK\r\n\r\n")
    client.send("Hello, World")

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1',8080))
    sock.listen(5)

    while True:  # wait for connecting by client
        connection, address = sock.accept()  # get client ip address and port
        handle_request(connection)
        connection.close()

if __name__ == '__main__':
    main()

