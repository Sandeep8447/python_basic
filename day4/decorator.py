import time
def log(func):
    def wrapper(*args, **kw):
        print 'call' + func.__name__ + '()...'
        return  func(*args, **kw)
    return wrapper

def performance(f):
    def print_time(*args, **kw):
        print 'call '+f.__name__+'() in '+time.strftime('%Y-%m-%d',time.localtime(time.time()))
        return f(*args,**kw)
    return print_time

@log
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)

@performance
def factorial2(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial2(10)