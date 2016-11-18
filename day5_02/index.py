# -*- coding:utf-8 -*-
__auth__ = 'christian'

from day5_02.model.admin import Admin

def login():
    user = raw_input('username:')
    pwd = raw_input('password:')
    admin = Admin()
    result = admin.CheckValidate(user, pwd,)
    if not result:
        print '用户名密码错误。'
    else:
        print 'welcome back %s'


if __name__ == '__main__':
    login()


