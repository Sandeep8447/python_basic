# -*- coding:utf-8 -*-
__auth__ = 'christian'

import paramiko

# get RSA private key
ssh_private_key = paramiko.RSAKey.from_private_key_file('id_rsa')

# create a ssh object
ssh = paramiko.SSHClient()  # is instance

# allow to connect some host do not in the know_hosts file.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # add fingerprint

# connect the server
ssh.connect(hostname='192.168.11.90', port=22, username='root', pkey=ssh_private_key)

# excu the unix-like command
stdin, stdout, stderr = ssh.exec_command('free -h; ip a')

res, err = stdout.read(), stderr.read()

# get the results
result = res if res else err
print result

# close the conection
ssh.close()