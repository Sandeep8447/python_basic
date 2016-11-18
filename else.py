def average(*args):
    s=0.0
    l=len(args)
    if l==0:
        return s
    for x in args:
        s+=x
    return s
print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)

def Person(**kwargs):
    print kwargs
    if kwargs.has_key("name"):
        print kwargs["name"]
    else:
        print "must input name arg"
Person(name="duanlian", age=20, job='IT')



a = range(10)
print dir(a)
print all(a)
print any(a)
# if type(a) is list
print isinstance(a, list)


