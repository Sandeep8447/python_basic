'''
def cacl(n):
    print '--->', n
    if n/2 > 0:
        return cacl(n/2)
    return n
print cacl(12)
'''

data_list = range(0, 100000, 2)

def binary_search(find_num, data):
    mid = len(data) / 2
    if mid > 0:
        if find_num > data[mid]:
            print "data should in right", mid
            binary_search(find_num, data[mid:])
        elif find_num < data[mid]:
            print "data should in left", mid
            binary_search(find_num, data[:mid])
        else: # find num equals to mid
            print "find the num: %s" % data[mid]
    elif mid == 0:
        print "find the num: %s" % data[mid]
    else:
        print 'cannot find the num', find_num

if __name__ == '__main__':
    find_n = raw_input("find:").strip()
    if find_n.isdigit():
        find_n = int(find_n)
        binary_search(find_n, data_list)