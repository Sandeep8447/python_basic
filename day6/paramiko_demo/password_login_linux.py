# -*- coding:utf-8 -*-
__auth__ = 'christian'

import paramiko

# create a ssh object
ssh = paramiko.SSHClient()  # is instance

# allow to connect some host do not in the know_hosts file.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # add fingerprint

# connect the server
ssh.connect(hostname='192.168.11.90', port=22, username='root', password='123456')

# executing  the unix-like command
stdin, stdout, stderr = ssh.exec_command('free -h')

res, err = stdout.read(), stderr.read()

# get the results
result = res if res else err
print result

# close the conection
ssh.close()