class myException(Exception):
    pass

try:
    name = 'chris'
    name_list = ['alex', 'eric']

    raise myException
except NameError, err:
    print err
except IndexError,err:
    print err
