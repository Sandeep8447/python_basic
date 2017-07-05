# -*- coding:utf-8 -*-
__auth__ = 'christian'

# The Pipe() function returns a pair of connection objects connected by a pipe which by default is duplex (two-way)
'''
The two connection objects returned by Pipe() represent the two ends of the pipe. 
Each connection object has send() and recv() methods (among others). 
Note that data in a pipe may become corrupted if two processes (or threads) try to read from 
or write to the same end of the pipe at the same time.
Of course there is no risk of corruption from processes using different ends of the pipe at the same time.
'''
from multiprocessing import Process, Pipe


def f(conn):
    conn.send([42, None, 'hello from child'])
    conn.send([42, None, 'hello from child'])
    print ('from parent_conn:', conn.recv())
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # prints "[42, None, 'hello']"
    print(parent_conn.recv())  # prints "[42, None, 'hello']"
    parent_conn.send('hello chris')
    p.join()