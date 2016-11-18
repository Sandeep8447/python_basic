# -*- coding:utf-8 -*-
__auth__ = 'christian'
import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='', port=3306)  # create connection
    cur = conn.cursor()  # create cursor
    cur.execute('create database if not exists python')
    conn.select_db('python')
    cur.execute('create table if not exists test(id int,info varchar(20))')

    value = [1, 'hi rollen']
    sql = 'insert into test values(%s,%s)'
    cur.execute(sql, value)
    print cur.lastrowid  # get incremental id
    # values = []
    # for i in range(20):
    #     values.append((i, 'hi rollen' + str(i)))
    #
    # cur.executemany('insert into test values(%s,%s)', values)  # execute many
    #
    # cur.execute('update test set info="I am rollen" where id=3')
    # print cur.lastrowid
    conn.commit()  # commit data if you change data
    cur.close()
    conn.close()

except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
