# -*- coding:utf-8 -*-

import types


def json_get(json, l_key, default):
    ret = json
    for k in l_key:
        if type(k) is types.IntType:
            if k < 0:
                return default
            if not (type(ret) is types.ListType):
                return default
            if len(ret) <= k:
                return default
        elif type(k) is types.StringType:
            if not (type(ret) is types.DictType):
                return default
            if not ret.has_key(k):
                return default
        else:
            return default
        ret = ret[k]

    return ret

# menu = ["Momo", "Stamp"]
menu = {
    'Beijing': {
        "ChaoYang": {
            "CBD": ['CICC', 'CCTV'],
            "JinRongJie": [""],
            "WangJing": ["Momo", "Stamp"]
        },
        "HaiDian": ['Baidu', 'Youku']
    },

    'Shanghai': {
        "PuDong": ['Ctrip', '1 Shop'],
        "PuXi": ['China Bank', 'Amerian Bank']
    }
}
#
# # for key in menu.keys():
#     print key
# first_level = raw_input("please chosen:")
# for key in menu[first_level].keys():
#     print key
# second_level = raw_input("please chosen:")
# for value in menu[first_level][second_level]:
#     print value
# third_level = raw_input("Please chosen:")
# print "Welcome to %s!" % third_level


for menuItem in menu:
    print menuItem
while True:
    sub_menu = raw_input("please chosen submenu:").strip()
    if type(menu) is types.ListType:
        if sub_menu not in menu:
            print "Wrong, please chosen again."
            continue
        print "Welcome to %s!" % sub_menu
        break
    if type(menu[sub_menu]) is types.DictType:
        for key in menu[sub_menu].keys():
            print key
    if type(menu[sub_menu]) is types.ListType:
        for value in menu[sub_menu]:
            print value
        sub_menu = raw_input("please chosen submenu:").strip()
        print "Welcome to %s!" % sub_menu
        break
    # if type(sub_menu) is types.StringType:
    #     print "Welcome to %s!" % sub_menu
    #     break
    menu = menu[sub_menu]


exit_flag = False
while not exit_flag:
    for index,key in enumerate(menu.keys()):
        print index,key
    choice_1 = raw_input("please choose menu to enter:").strip()
    if choice_1.isdigit():
        choice_1 = int(choice_1)
        key_1 = menu.keys()[choice_1]
        print '---',key_1
        while not exit_flag:
            for index,key in enumerate(menu[key_1]):
                print index,key
            choice_2 = raw_input("please choose menu to enter:").strip()
            if choice_2.isdigit():
                choice_2 = int(choice_2)
                key_2 = menu[key_1].keys()[choice_2]
                while not exit_flag:
                    for index, key in enumerate(menu[key_1][key_2]):
                        print '------',index,key
                    choice_3 = raw_input("please choose menu to enter:").strip()
                    if choice_3.isdigit():
                        print "this is the last level..."
                    elif choice_3 == 'quit':
                        exit_flag = True
                    elif choice_3 == 'back':
                        break
else:
    print '--------going to quit---------'