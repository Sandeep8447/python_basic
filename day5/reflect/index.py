# -*- coding:utf-8 -*-
__auth__ = 'christian'


'''
规范： ***.***
依据URL的不同，响应不同的请求
'''
'''
from backend import account
# account/login
url = raw_input("请输入url:")
array = url.split('/')
if url == "account/login":
    account.login()
elif url == "account/logout":
    account.logout()
'''

'''
from backend import account

def run():
    url = raw_input("请输入url：").strip()
    func = getattr(account, url)  # import login
    func()

if __name__ == '__main__':
    run()
'''
'''
from backend import account
def run():
    url = raw_input("请输入url：").strip()
    if hasattr(account, url):
        func = getattr(account, url)  # import login
        func()
    else:
        print("404")

if __name__ == '__main__':
    run()
'''
# def run():
#     url = raw_input("请输入url：")
#     module, func = url.split('/')
#     user_spance = __import__('backend.' + module)  # import backend
#     model = getattr(user_spance, module)  # import account
#     if hasattr(model, func):
#         func = getattr(model, func)
#         func()
#     else:
#         print("404")
# if __name__ == '__main__':
#      run()

# def run():
#     url = raw_input("请输入您想访问页面的url:").strip()
#     #url = "account/login"
#     modules, func = url.split("/")
#     model = __import__("backend." + modules, fromlist=True)  # 注意fromlist参数
#     if hasattr(model, func):
#         func = getattr(model, func)
#         func()
#     else:
#         print("404")
# if __name__ == '__main__':
#      run()

'''
url = "backend/account/login"
array = url.split("/")
print array  # ['backend', 'account', 'login']
print array[:-1]
print '.'.join(array)  # backend.account.login
'''

def run():
    url = raw_input("请输入您想访问页面的url:").strip()
    #url = "backend/account/login"
    array = url.split("/")
    #model = __import__('.'.join(array[:-1]), fromlist=True)  # 注意fromlist参数
    model = __import__('.'.join(array[:-1]), fromlist=[array[-1]])  # 注意fromlist参数
    if hasattr(model, array[-1]):
        func = getattr(model, array[-1])
        func()
    else:
        print("404")

if __name__ == '__main__':
     run()
