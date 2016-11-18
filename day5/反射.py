__author__ = 'jieli'



class myClass(object):

    def fax(self):
        print 'faxing....'
    def copy(self):
        print 'copying...'

def printing():
    print 'printing....'

m = myClass()
if hasattr(m,'fax'):
    func = getattr(m,'fax')
    func()

setattr(m,'print2',printing)
m.print2()

try:
    #delattr(m,'copy')
    #print name
    #print dfdf
    #print tttt
    print m
except AttributeError,e:
    print 'something wrong..',e

except Exception,e:
    print e

finally:
    print '-----------'
#else:
#    print "print nothing wrong ...."