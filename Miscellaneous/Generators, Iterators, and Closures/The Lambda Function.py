# A lambda function is a function without a name (you can also call it an anonymous function).

two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 5):
    print(sqr(a), end=" ")
    print(pwr(a, two()))

""" the first lambda is an anonymous parameterless function that always returns 2. As we've assigned it to a
 variable named two, we can say that the function is not anonymous anymore, and we can use the name to invoke it.

the second one is a one-parameter anonymous function that returns the value of its squared argument. 
We've named it as such, too.

the third lambda takes two parameters and returns the value of the first one raised to the power of the second one. 
The name of the variable which carries the lambda speaks for itself. We don't use pow to avoid confusion with 
the built-in function of the same name and the same purpose."""


def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


# def poly(x):
#     return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

# ---------------------------------------------------------------------------------------------------------------------

list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)
# [1, 2, 4, 8, 16]

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()
# 1 4 16 64 256

# ---------------------------------------------------------------------------------------------------------------------
from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)

# ---------------------------------------------------------------------------------------------------------------------


def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power


fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))
