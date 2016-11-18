# -*-coding:utf-8-*-
products = [
    ['Iphone', 8000],
    ['ipad', 5000],
    ['Tesla', 30000],
    ['Coffee', 35],
    ['Clothes', 500],
    ['Shoes', 800],
]

salary = 9000
shop_list = []
while True:
    for index,p in enumerate(products):
        print index, p[0], p[1]
    choice = raw_input("Choose something to buy：").strip()
    if choice.isdigit():
        choice = int(choice)
        p_price = products[choice][1]
        if p_price < salary:
            shop_list.append(products[choice])
            salary -= p_price
            print "Has add \033[31;1m%s\033[0m into shop list, your current balance is \033[31;1m%s\033[0m" % (products[choice][0], salary)
        else:
            print "\033[41;1mMoney is not enough, try sth else.\033[0m"
    elif choice == 'quit':
        print '----------shopping list-------------'
        for k,v in enumerate(shop_list):
            print k,v
        print "Your current balance is \033[41;1m%s\033[0m" % salary
        print '-------------Bye--------------------'
        break