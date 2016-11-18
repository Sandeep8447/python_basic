# -*- coding:utf-8 -*-
import os

def CheckUserName(username):
    flag = False
    lockfile = "D:\\lockfile.txt"
    if os.path.exists(lockfile):
        fileHandle = open(lockfile,'r')
        names = fileHandle.readlines()
        for i in names:
            if i == username:
                flag = True
                break
        fileHandle.close()
    if flag:
        return True
    else:
        return False

def LockUserName(username):
    lockfile = "D:\\lockfile.txt"
    fileHandle = open(lockfile, 'w')
    fileHandle.write(username)
    fileHandle.close()

user_data = {
    'christian': '12345',
    'Alex': 'hello',
    'James': 'world'
}
login_count = 3
while login_count > 0:
    user_name = raw_input("Please input you username:").strip()
    password = raw_input("Please input you password:")
    if not CheckUserName(user_name):
        if not user_data.has_key(user_name):
            print "Wrong. Please Check you username, and input again."
            continue
        if password == user_data.get(user_name):
            print "hello, %s Welcome back!" % user_name
            break
        else:
            login_count -= 1
            print "Wong password, please try again."
            print "you can try %d times" % login_count
            if not login_count:
                print "Sorry, you username is locked."
                LockUserName(user_name)
            continue
    else:
        print "Sorry, your username is locked!"
        break