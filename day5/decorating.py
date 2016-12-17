def login(func):
    def wrapper(args):
        print "---do sth before run func"
        return func(args)
    return wrapper

@login
def sayhi(name):
    print "hello, %s" %name


sayhi("chris")