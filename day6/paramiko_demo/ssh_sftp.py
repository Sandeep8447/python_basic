# -*- coding:utf-8 -*-
__auth__ = 'christian'

import paramiko

# create a ssh object
transport = paramiko.Transport(('192.168.11.90', 22,))  # is instance

# connect the server
transport.connect(username='root', password='123456')

sftp = paramiko.SFTPClient.from_transport(transport)

sftp.put('/root/sayhi.txt', '/tmp/hello.txt')

# sftp.get('remove_path', 'local_path')
sftp.get('/tmp/hello.txt', '/root/hello.txt')

transport.close()