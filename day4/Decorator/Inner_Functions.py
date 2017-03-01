# -*- coding:utf-8 -*-
__auth__ = 'christian'

def outer(num1):
    def inner_increment(num1):  # hidden from outer code
        return num1 + 1
    num2 = inner_increment(num1)
    print (num1, num2)

'''
Encapsulation:
You use inner functions to protect them from anything happening outside of the function,
meaning that they are hidden from the global scope.
'''
#inner_increment(10)
outer(10)


'''
Keep in mind that this is just an example. Although this code does achieve the desired result,
it’s probably better to make the inner_increment() function a top-level “private” function
using a leading underscore: _inner_increment().
'''

'''The following recursive example is a slightly better use case for a nested function:'''
def factorial(number):

    # error handling
    if not isinstance(number, int):
        raise TypeError("Sorry. 'number' must be an integer.")
    if not number >= 0:
        raise ValueError("Sorry. 'number' must be zero or positive.")

    def inner_factorial(number):
        if number <= 1:
            return 1
        return number*inner_factorial(number-1)
    return inner_factorial(number)

# call the outer function
print(factorial(4))

'''
Test this out as well. One main advantage of using this design pattern is
that by performing all argument checking in the outer function,
you can safely skip error checking altogether in the inner function.
'''


'''
Keepin’ it DRY
Perhaps you have a giant function that performs the same chunk of code in numerous places.
For example, you might write a function which processes a file,
and you want to accept either an open file object or a file name:
'''

def process_1(file_name):
    def do_stuff(file_process):
        for line in file_process:
            print(line)
    if isinstance(file_name, str):
        with open(file_name, 'r') as f:
            do_stuff(f)
    else:
        do_stuff(file_name)


def process(file_name):

    def do_stuff(file_process):
        wifi_locations = {}

        for line in file_process:
            values = line.split(',')
            # Build the dict, and increment values
            wifi_locations[values[1]] = wifi_locations.get(values[1], 0) + 1

        max_key = 0
        for name, key in wifi_locations.items():
            all_locations = sum(wifi_locations.values())
            if key > max_key:
                max_key = key
                business = name
        print('There are {0} WiFi hot spots in NYC and {1} has the most with {2}.'.format(
            all_locations, business, max_key))

    if isinstance(file_name, str):
        with open(file_name, 'r') as f:
            do_stuff(f)
    else:
        do_stuff(file_name)


process("NYC_Wi-Fi_Hotspot_Locations.csv")

'''Closures and Factory Functions'''

'''
What’s a closure?
A closure simply causes the inner function to remember the state of its environment when called. Beginners often think
that a closure is the inner function, when it’s really caused by the inner function.
The closure "closes" the local variable on the stack and this stays around after the the stack creation has finished executing.
'''

def generate_power(number):
    """
    Examples of use:

    >>> raise_two = generate_power(2)
    >>> raise_three = generate_power(3)
    >>> print(raise_two(7))
    128
    >>> print(raise_three(5))
    243
    """

    # define the inner function ...
    def nth_power(power):
        return number ** power
    # ... which is returned by the factory function

    return nth_power

raise_two = generate_power(2)
print(raise_two(7))
raise_three = generate_power(3)
print(raise_three(5))


'''
What’s happening here?
The ‘generate_power()’ function is a factory function – which simply means
that it creates a new function each time it is called and then returns the newly created function.
Thus, raise_two and raise_three are the newly created functions.
What does this new, inner function do? It takes a single argument, power, and returns number**power.
Where does the inner function get the value of number from? This is where the closure comes into play:
nth_power() gets the value of power from the outer function, the factory function. Let’s step through this process:

Call the outer function: generate_power(2)
Build the nth_power() function which takes a single argument power
Take a snapshot of the state of nth_power() which includes number=2
Pass that snapshot into the generate_power() function
Return the nth_power() function
Put another way, the closure functions to "initialize" the number bar in the nth_power() function and then returns it.
Now, whenever you call that newly returned function, it will always see its own private snapshot that includes number=2.
'''

def has_permission(page):
    def inner(username):
        if username == 'Admin':
            return "'{0}' does have access to {1}.".format(username, page)
        else:
            return "'{0}' does NOT have access to {1}.".format(username, page)
    return inner


current_user = has_permission('Admin Area')
print(current_user('Admin'))

random_user = has_permission('Admin Area')
print(current_user('Not Admin'))

'''
This is a simplified function to check if a certain user has the correct permissions to access a certain page.
You could easily modify this to grab the user in session to check if they have the correct credentials to access a certain route.
Instead of checking if the user is just equal to ‘Admin’, you could query the database to check the permission
then return the correct view depending on whether the credentials are correct or not.
'''

'''
Conclusion
The use of closures and factory functions is the most common, and powerful, use for inner functions. In most cases,
when you see a decorated function, the decorator is a factory function which takes a function as argument,
and returns a new function which includes the old function inside the closure. Stop. Take a deep breath. Grab a coffee.
Read that again.

Put another way, a decorator is just syntactic sugar for implementing the process outlined in the generate_power() example.

I’ll leave you with an example:
'''

def generate_power(exponent):
    def decorator(f):
        def inner(*args):
            result = f(*args)
            return exponent**result
        return inner
    return decorator


@generate_power(2)
def raise_two(n):
    return n

print(raise_two(7))


@generate_power(3)
def raise_three(n):
    return n

print(raise_two(5))