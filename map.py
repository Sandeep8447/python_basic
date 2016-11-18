def f(x):
    return x**2
print map(f, range(10))

print map(lambda x:x**2, range(10))

def format_name(s):
    return s.capitalize()
print map(format_name, ['adam', 'LISA', 'barT'])

def format_name(s):
    return s[0].upper() + s[1:].lower()
print map(format_name, ['adam', 'LISA', 'barT'])