# -*- coding:utf-8 -*-
__auth__ = 'christian'

import paramiko

ssh = paramiko.SSHClient() # isinstance
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # sign
ssh.connect(hostname= '192.168.1.109', port=22, username='hrg', password='hrg123')
stdin, stdout, stderr = ssh.exec_command('free -h')
print stdout.read()
ssh.close()