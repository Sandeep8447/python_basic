# -*- coding:utf-8 -*-
__auth__ = 'christian'

import MySQLdb
from homework_day5 import conf

class MysqlHelper(object):

    def __init__(self):
        self.__conn_dict = conf.conn_dict  # create connection

    def GetSimple(self, sql, params):
        ''' 获取单条语句
        :param sql:
        :param params:
        :return:
        '''
        conn = MySQLdb.connect(**self.__conn_dict)  # create connection magic function
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)  # create cursor
        cur.execute(sql, params)
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data

    def GetDict(self, sql, params):
        ''' 获取多条数据（字典类型）'''
        conn = MySQLdb.connect(**self.__conn_dict)  # create connection
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)  # create cursor
        cur.execute(sql, params)
        data = cur.fetchone()
        cur.close()
        conn.close()
        return data

    def InsSample(self, sql, params):
        '''插入单条数据
        :param sql:
        :param params:
        :return:
        '''
        conn = MySQLdb.connect(**self.__conn_dict)  # create connection
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)  # create cursor
        count = cur.execute(sql, params)
        count.commit()
        count.close()
        count.close()
        return count

    def InsSample_ReturnID(self, sql, params):
        '''插入单条数据
        :param sql:
        :param params:
        :return:
        '''
        conn = MySQLdb.connect(**self.__conn_dict)  # create connection
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)  # create cursor
        cur.execute(sql, params)
        id = cur.lastrowid
        cur.close()
        conn.close()
        return id