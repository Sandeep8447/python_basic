# -*- coding:utf-8 -*-
__auth__ = 'christian'

from initial_account import *  #导入初始化账号信息模块
import pickle
import re
import time

def read_account():
    with open("account.txt", "rb") as handle:
        account_dict = pickle.load(handle)
    return account_dict

def recoding_login_error_count(user_account, login_error_count):
    account_dict = read_account()
    account_dict[user_account][1] = login_error_count
    write_account(account_dict)  #调用initial_account模块函数，将当前字典状态写入文件


#输入银行卡号的函数
def verify_account():
    while True:
        user_account = raw_input("请输入银行卡号：").strip()
        if user_account not in account_dict:  #判断卡号是否存在
            print "\033[31;2m请输入正确银行卡号：\033[0m"
            continue
        else:
            return user_account

def Verify_password(user_account):
    login_flag = False
    login_error_count = account_dict[user_account][1]
    while True:
        if login_error_count == 3:
            print "\033[31;2m你的账号已被锁定！\033[0m"
            break
        password = raw_input("请输入银行卡密码：").strip()
        if len(password) == 0:
            print "\033[31;2m密码不能为空\033[0m"
            continue
        if password != account_dict[user_account][0]:
            login_error_count += 1
            recoding_login_error_count(user_account, login_error_count)
            print "密码错误，请重新输入！还有%d次机会" % (3 - login_error_count)
            continue
        else:
            print "\033[32;1m登录成功！\033[0m"
            login_error_count = 0
            recoding_login_error_count(user_account, login_error_count)
            login_flag = True
        return login_flag

def check_lock(user_account):  #检查锁记录函数
    if account_dict[user_account][1] == 3:
        print "\033[31;1m你的账号已被锁定！\033[0m"
    else:
        pass

#交易明细函数，flag为0时为记录，flag为1时为读取
def trade_detail(user_account, tran_type = "", amount = "", interest = "", balance = "", flag = 1):
    with file("trade_detail.txt","a") as f:
        if flag == 0:
            f.write('%-8s %10s %8s %8s %6s %3s %7s\n' % (user_account,time.strftime('%Y-%m-%d'),
                                                       time.strftime('%H:%M:%S'), tran_type,amount,interest,balance))
        else:
            print '%s %s %s %s %s %s %s\n'%('卡号','日期','时间','交易类型','金额','利息','余额')
            with file("trade_detail.txt") as f:
                for line in f.xreadlines():
                    if user_account in line:
                        print line
            raw_input("按任意键返回")

def balance_query(user_account, flag = True):
    balance = account_dict[user_account][2]
    cash = account_dict[user_account][3]
    interest = "%5"  # 利息为5%
    if flag:
        print "你本月余额为\033[34;2m%d\033[0m。(可取现\033[34;2m%d\033[0m，利息\033[33;2m%s\033[0m)" %(balance,
                                                                                           cash, interest)
        time.sleep(1)
    return balance, cash

def withdrawal(user_account):
    choice_money = [100,200,500,1000,2000,3000]
    while True:
        print "请输入取款金额('0'退出)："
        for i in choice_money:
            print i
        input_money = raw_input("--->").strip()
        if input_money == "0":
            break
        elif input_money.isdigit() == False or int(input_money) not in choice_money:  #判断取款金额是否合法
            print "\033[31;2m请输入正确取款金额！\033[0m"
        else:
            balance, cash = balance_query(user_account)  #调用查询余额函数
            balance = balance - int(input_money)*1.05 #扣款和利息
            cash = cash - int(input_money)  #更新取现额度
            if balance > 0 and cash > 0:
                account_dict[user_account][1] = balance
                account_dict[user_account][2] = cash
                write_account(account_dict)
                print "\033[32;1m取款成功！\033[0m"
                time.sleep(2)
                trade_detail(user_account, "取现", str(-int(input_money)), str(int(input_money) * 0.05), str(balance),
                             0)  # 调用交易明细函数，将交易明细写入文件
            elif balance <= 0:
                print "\033[31;2m你的余额不足！\033[0m"
            elif cash < 0:
                print "\033[31;2m取现额度超过上限！\033[0m"
            balance_query(user_account)  #显示取款操作后的余额信息

def transfer_accounts(user_account):
    while True:
        other_account = verify_account()
        if other_account == user_account:
            print "\033[31;2m不能对自己转账！\033[0m"
            continue
        confirm_account = raw_input("请再次输入对方银行卡号：")
        if other_account != confirm_account:
            print "\033[31;2m两次输入的银行卡号不一致！\033[0m"
        else:
            while True:
                transfer_money = raw_input("请输入转账金额('0'退出)：")
                if transfer_money.isdigit() == False:
                    print "\033[31;2m请输入数字！\033[0m"
                    continue
                if transfer_money == 0:
                    break
                balance, cash = balance_query(user_account)
                if int(transfer_money) > balance:
                    print "\033[31;2m你的余额不足！\033[0m"
                    continue
                else:
                    account_dict[user_account][1] -= int(transfer_money)
                    account_dict[other_account][1] += int(transfer_money)
                    write_account(account_dict)
                    print "\033[32;1m转账成功！\033[0m"
                    time.sleep(2)
                    trade_detail(user_account, "转出", str(-int(transfer_money)), "0", account_dict[user_account][2], 0)  # 记录转出明细
                    trade_detail(other_account, "转入", transfer_money, "0", account_dict[other_account][2],
                                 0)  # 记录对方转入明细
                    balance_query(user_account)
                    break

def repay(user_account):  #还款
    account_data = read_account()
    balance = account_data[user_account][2]
    repay_money = 15000 - balance
    if repay_money == 0:
        print "\033[31;2m你本月无需还款\033[0m"
    else:
        while True:
            input_money = raw_input("你本月支出\033[31;2m%d\033[0m元，请输入还款金额:" % repay_money).strip()
            if input_money.isdigit() == False:
                print "\033[31;2m请输入数字\033[0m"
                continue
            input_money = int(input_money)
            if input_money == 0:
                break
            if input_money > repay_money:
                print "\033[31;2m请输入正确金额\033[0m"
                continue
            balance += repay_money
            account_dict[user_account][2] += balance  #更新余额
            write_account(account_data)
            trade_detail(user_account, "还款", str(input_money), "0", balance, 0) #记录
            print  "\033[32;1m还款成功！\033[0m"
            time.sleep(1.5)
            if balance == 15000:
                print "\033[32;1m你本月账单已还清！\033[0m"
                time.sleep(2)
            break


def billing(user_account): #生产账单
    bill_dict = {}
    bill_date = time.strftime("%Y-%m-%d")
    '''
    if -30 not in bill data
    '''
    re_date = re.search("\d+\-\d*\-",bill_date).group()
    f = file("trade_detail.txt")
    for i in f.readlines():
        if re_date in i and user_account in i:
            # 以交易类型作为key，将交易金额作为values的第一个列表元素
            bill_dict.setdefault(i.split()[3], [[], []])[0].append(int(i.split()[4]))
            # 以交易类型作为key，将利息作为values的第二个列表元素
            bill_dict.setdefault(i.split()[3], [[], []])[1].append(float(i.split()[5]))
            print "您本月账单如下："
            print re_date[:-1]  # 打印年-月
            print "%-12s%12s%13s" % ("交易类型", "金额", "利息")
            for i in bill_dict:
                # 会总各交易类型金额和利息并打印
                print "%-12s%8s%11s" % (i, reduce(lambda x, y: x + y, bill_dict[i][0]),
                                        reduce(lambda x, y: x + y, bill_dict[i][1]))
            balance = account_dict[user_account][2]
            if balance < 15000:
                choice = raw_input("您本月还需还款\033[31;2m%d\033[0m元，是否还款？(y)"%(15000 - balance))
                if choice == "y":
                    repay(user_account)  # 调用还款函数
            else:
                print "\033[32;1m您本月账单已清\033[0m"
                time.sleep(2)

#交易明细函数，flag为0时为记录，flag为1时为读取
def trade_list(user_account,tran_type = "",amount = "",interest = "",balance = "",flag = 1):
    with file("trade_detail.txt", 'a') as f:
        if flag == 0:
            f.write('%-8s %10s %8s %8s %6s %3s %7s\n'%(user_account, time.strftime('%Y-%m-%d'),
                                                       time.strftime('%H:%M:%S'),
                                                       tran_type, amount, interest, balance))
        else:
            print '%s %s %s %s %s %s %s\n' % ('卡号', '日期', '时间', '交易类型', '金额', '利息', '余额')
            with file("trade_detail.txt") as f:
                for line in f.xreadlines():
                    if user_account in line:
                        print line
            raw_input("按任意键返回")

def login_ATM():
    account_data = read_account()
    user_account = verify_account()
    if account_data[user_account][1] == 3:
       print "\033[31;2m你的账号已被锁定！\033[0m"
    else:
        flag = Verify_password(user_account)
        return account_data, user_account, flag

def shopping_interface(payment):
    payment_flag = False
    account_data, user_account, login_flag = login_ATM()
    choice = raw_input("确定支付\33[31;2m%d\033[0m元？(y)"%payment)
    if choice == 'y':
        balance, cash = balance_query(user_account)
        if balance > payment:
            balance -= payment
            account_data[user_account][2] = balance
            write_account(account_data)
            trade_detail(user_account, "shopping", str(-payment), "0", balance, 0)
            print "\033[32;1m支付成功！\033[0m"
            time.sleep(2)
            payment_flag = True
        else:
            print "\033[31;2m你银行卡中的余额不足！\033[0m"
    return payment_flag

if __name__ == '__main__':
    print "******************欢迎进入银行系统*********************"
    account_dict,user_account,login_flag = login_ATM()
    if login_flag:
        while True:
            print "******************请选择操作菜单******************"
            print '1.查询\n2.取现\n3.转账\n4.还款\n5.明细\n6.账单\n0.退出'
            choice = raw_input("--->")
            if choice == "0":
                break
            elif choice == "1":
                balance_query(user_account, choice)
            elif choice == "2":
                withdrawal(user_account)
            elif choice == "3":
                transfer_accounts(user_account)
            elif choice == "4":
                repay(user_account)
            elif choice == "5":
                trade_detail(user_account)
            elif choice == "6":
                billing(user_account)