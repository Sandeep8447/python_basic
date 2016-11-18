# -*-coding:utf-8-*-

products = [
        "bike",
        "coffee",
        "cake",
        "rose",
        "milk",
        "television"
]

prices = [
    4000,
    35,
    150,
    180,
    80,
    5000,
]
goodsList = []
salary = raw_input("please input you salary:").strip()
countOfGoods = len(products)
total = 0

print "------------GOODS------------"
for i in products:
    print i,
print "\n-----------------------------"

while True:
    goods = raw_input("\n please chosen the product you want:").strip()
    if goods in products:
        total += prices[products.index(goods)]
        if total < int(salary):
            goodsList.append(goods)
        else:
            total -= prices[products.index(goods)]
            print "sorry, you do not have enough money."
        print total
    elif goods == 'q':
        balance = int(salary) - total
        if goodsList:
            print "the goods you buy:"
            for i in goodsList:
                print i,
            print " you balance：%d yuan." % balance
            break
        else:
            print "you do not buy anything."
    else:
        print "%s do not exits, please chosen again." % goods




