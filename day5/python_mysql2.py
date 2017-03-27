# -*- coding:utf-8 -*-
__auth__ = 'christian'

import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', port=3306)
    cur = conn.cursor()
    #cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)  # show data like {'info': 'hi rollen', 'id': 1L} as dictionary
    conn.select_db('python')  # chose one database
    count = cur.execute('select * from test')  # show the rows affected
    print 'there has %s rows record' % count

    result = cur.fetchone()  # fetch one row you want
    print result
    print 'ID: %s info %s' % result
    results = cur.fetchmany(5)  # fetch some data you want
    for r in results:
        print r
    print '==' * 10
    cur.scroll(0, mode='absolute')  # absolute location
    #cur.scroll(1, mode='relative')  # relative location

    results = cur.fetchall()  # fetch all data, get all data in one table
    print result
    for r in results:
         print r[1]
    print '==' * 10
    print cur.lastrowid
    conn.commit()  #
    cur.close()  # disconnect cursor
    conn.close()  # disconnect mysql

except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
