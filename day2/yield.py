def run():
    for i in range(100):
        print '--->',i
        yield i

task = run()
print task.next()
print "do something else....."
print task.next()
print "do something else....."
print task.next()
print "do something else....."
print task.next()
print "do something else....."
print task.next()
print "do something else....."
print task.next()
print "do something else....."
print task.next()

