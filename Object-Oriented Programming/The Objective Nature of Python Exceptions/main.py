""" More about exceptions"""

# ----------------------------------------------------- Example 1 -----------------------------------------------------

print("Example 1".center(40, '-'))


def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        return None
    else:
        print("Everything went fine")
        return n


print(reciprocal(2))  # Everything went fine \n 0.5
print(reciprocal(0))  # Division failed \n None

""" A code labelled in this way is executed when (and only when) no exception has been raised inside the try: part. 
    We can say that exactly one branch can be executed after try: - either the one beginning with except 
    (don't forget that there can be more than one branch of this kind) or the one starting with else.

Note: the else: branch has to be located after the last except branch."""

# ---------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------- Example 2 -----------------------------------------------------

print("Example 2".center(40, '-'))


def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        n = None
    else:
        print("Everything went fine")
    finally:
        print("It's time to say goodbye")
        return n


print(reciprocal(2))  # Everything went fine \n It's time to say goodbye \n 0.5
print(reciprocal(0))  # Division failed \n It's time to say goodbye \n None

""" Note: these two variants (else and finally) aren't dependent in any way, 
    and they can coexist or occur independently.

    The finally block is always executed (it finalizes the try-except block execution, hence its name), 
    no matter what happened earlier, even when raising an exception, no matter whether this has been handled or not."""
# ---------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------- Exceptions are classes -----------------------------------------------

""" Note: the identifier's scope covers its except branch, and doesn't go any further.

The example presents a very simple way of utilizing the received object - just print it out (as you can see, the output
is produced by the object's __str__() method) and it contains a brief message describing the reason.

The same message will be printed if there is no fitting except block in the code, and Python is forced to handle 
it alone."""


# Note: [!] exceptions are classes


print("Exceptions are classes".center(40, '-'))

try:
    i = int("Hello!")
except Exception as e:
    print(e)
    print(e.__str__())

""" As you can see, the except statement is extended, and contains an additional phrase starting with the as keyword,
    followed by an identifier. The identifier is designed to catch the exception object so you can analyze its nature 
    and draw proper conclusions."""

# ---------------------------------------------------------------------------------------------------------------------


# -------------------------------------------- Exceptions are classes 2 -----------------------------------------------

print("2) Exceptions are classes".center(40, '-'))


def print_exception_tree(thisclass, nest=0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)


print_exception_tree(BaseException)
# ---------------------------------------------------------------------------------------------------------------------


# -------------------------------------- Detailed anatomy of exceptions -----------------------------------------------

print("Detailed anatomy of exceptions".center(40, '-'))


def print_args(args):
    lng = len(args)
    if lng == 0:
        print("")
    elif lng == 1:
        print(args[0])
    else:
        print(str(args))


try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=' : ' ,end=' : ')
    print_args(e.args)

print("\nThe End of First Try Block\n")

try:
    raise Exception("my exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

print("\nThe End of Second Try Block\n")

try:
    raise Exception("my", "exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

""" The BaseException class introduces a property named args. It's a tuple designed to gather all arguments 
    passed to the class constructor. It is empty if the construct has been invoked without any arguments,
    or contains just one element when the constructor gets one argument 
    (we don't count the self argument here), and so on."""

# ---------------------------------------------------------------------------------------------------------------------


# ------------------------------------ How to create your own exception -----------------------------------------------

# The exceptions hierarchy is neither closed nor finished, and you can always extend it if you want or
# need to create your own world populated with your own exceptions.

""" This is done by defining your own, new exceptions as subclasses derived from predefined ones."""


""" Note: if you want to create an exception which will be utilized as a specialized case of any built-in exception,
    derive it from just this one. If you want to build your own hierarchy, and don't want it to be closely connected
    to Python's exception tree, derive it from any of the top exception classes, like Exception."""

print("How to create your own exception".center(40, '-'))


class MyZeroDivisionError(ZeroDivisionError):
    pass


def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:
        raise ZeroDivisionError("some bad news")


for mode in [False, True]:
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print('Division by zero')

for mode in [False, True]:
    try:
        do_the_division(mode)
    except MyZeroDivisionError:
        print('My division by zero')
    except ZeroDivisionError:
        print('Original division by zero')

""" Demands like these may be fulfilled in the way presented in the editor. Look at the code, and let's analyze it:

   1)  We've defined our own exception, named MyZeroDivisionError, derived from the built-in ZeroDivisionError.
       As you can see, we've decided not to add any new components to the class.

   2)  In effect, an exception of this class can be - depending on the desired point of view - treated like a plain
       ZeroDivisionError, or considered separately.

   3)  The do_the_division() function raises either a MyZeroDivisionError or ZeroDivisionError exception,
       depending on the argument's value.

   4)  The function is invoked four times in total, while the first two invocations are handled using only
       one except branch (the more general one) and the last two ones with two different branches, able to distinguish 
       the exceptions (don't forget: the order of the branches makes a fundamental difference!) """

# ---------------------------------------------------------------------------------------------------------------------


# ------------------------------------ 3) How to create your own exception ---------------------------------------------
print()
print("3) How to create your own exception".center(40, '-'))


class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza


""" The TooMuchCheeseError exception needs more information than the regular PizzaError exception,
    so we add it to the constructor - the name cheese is then stored for further processing."""


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no such pizza on the menu")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "too much cheese")
    print("Pizza ready!")


for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)


# ---------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------ Key Takeaways ------------------------------------------------------

""" 1.  The else: branch of the try statement is executed when there has been no exception during the execution of the 
        try: block."""

""" 2.  The finally: branch of the try statement is always executed. """

""" 3.  The syntax except Exception_Name as an exception_object: lets you intercept an object carrying information about
        a pending exception. The object's property named args (a tuple) stores all arguments passed
        to the object's constructor."""


""" 4.  The exception classes can be extended to enrich them with new capabilities,
        or to adopt their traits to newly defined exceptions. [!] For Example: """

print("Key Takeaways".center(40, '-'))

try:
    assert __name__ == "__main__"
except:
    print("fail", end=' ')
else:
    print("success", end=' ')
finally:
    print("done")
# ---------------------------------------------------------------------------------------------------------------------
