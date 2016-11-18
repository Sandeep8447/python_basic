
def auth(func):
    def wrapper(*args, **kwargs):
        user = raw_input("input username:").strip()
        if user == 'chris':
            print "-------welcome login----------"
            func(*args, **kwargs)
        else:
            print "---------wrong passwd, access denied!-----------"
    return wrapper

@auth
def task(name,age=18):
    print "do something....", name,age


def task2():
    print "do something2...."


def task3():
    print "do something3...."

task("duanlian") # wrapper("chris")
task2()
task3()
