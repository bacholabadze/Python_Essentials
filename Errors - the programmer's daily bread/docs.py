""" Exceptions
Each time your code tries to do something wrong/foolish/irresponsible/crazy/unenforceable, Python does two things:

1) it stops your program;
2) it creates a special kind of data, called an exception.

Both of these activities are called raising an exception. We can say that Python always raises an exception
(or that an exception has been raised) when it has no idea what to do with your code."""

""" if nothing happens to take care of the raised exception, the program will be forcibly terminated, 
and you will see an error message sent to the console by Python;"""

# ValueError <= It's called exception name

# ---------------------------------- Example ---------------------------------------------------

""" This is how it works:

if the try branch raises the exc1 exception, it will be handled by the except exc1: block;
similarly, if the try branch raises the exc2 exception, it will be handled by the except exc2: block;
if the try branch raises any other exception, it will be handled by the unnamed except block.
"""

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")

# --------------------------------------------------------------------------------------------------

""" 
1)  the except branches are searched in the same order in which they appear in the code;
2)  you must not use more than one except branch with a certain exception name;
3)  the number of different except branches is arbitrary - the only condition is that if you use try, 
    you must put at least one except (named or not) after it;
4)  the except keyword must not be used without a preceding try;
5)  if any of the except branches is executed, no other branches will be visited;
6)  if none of the specified except branches matches the raised exception, the exception remains unhandled
7)  if an unnamed except branch exists (one without an exception name), it has to be specified as the last."""