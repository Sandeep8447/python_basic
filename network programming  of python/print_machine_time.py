# -*-coding:utf-8-*-
#!/usr/bin/env python
# Python Network Programming Cookbook
# This program is optimized for Python 2.7. It may run on amy
# other Python version with/without modifications.

import ntplib
from time import ctime

def print_time():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('pool.ntp.org')
    print ctime(response.tx_time)

if __name__ == '__main__':
    print_time()