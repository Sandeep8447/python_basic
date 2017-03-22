# -*- coding:utf-8 -*-
__auth__ = 'christian'

import MySQLdb
from homework_day5 import conf

class MysqlHelper(object):

    def __init__(self):
        self.__conn_dict = conf.conn_dict  # create connection

    def Get_Dict(self, sql, params):
        conn = MySQLdb.connect(**self.__conn_dict)  # create connection magic function
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)  # create cursor
        cur.execute(sql, params)
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data

    def Get_One(self, sql, params):
        conn = MySQLdb.connect(**self.__conn_dict)  # create connection
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)  # create cursor
        cur.execute(sql, params)
        data = cur.fetchone()
        cur.close()
        conn.close()
        return data