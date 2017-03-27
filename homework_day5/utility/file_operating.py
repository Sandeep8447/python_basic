# -*- coding:utf-8 -*-
__auth__ = 'christian'

from homework_day5.utility.sql_helper import MysqlHelper
import MySQLdb

class UserInfo(object):

    def __init__(self):
        self.__helper = MysqlHelper()

    def checklogin(self, name, pwd):
        conn = MySQLdb.connect(**self.__conn_dict)  # create connection magic function
        # show data like {'info': 'hi rollen', 'id': 1L} as dictionary
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)  # create cursor
        cur.execute(name, pwd)
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data

class ChatRecord(object):
    def __init__(self):
        pass

    def InsertRecord(self, message, date, userid):
        conn = MySQLdb.connect(**self.__conn_dict)  # create connection magic function
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)  # create cursor
        cur.execute(message, date, userid)
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data

    def GetRecord(self, userid):
        conn = MySQLdb.connect(**self.__conn_dict)  # create connection magic function
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)  # create cursor
        cur.execute(sql, params)
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
