""" The hierarchy of exceptions """

""" Python 3 defines 63 built-in exceptions, and all of them form a tree-shaped hierarchy, although the tree is a bit 
weird as its root is located on top."""

""" the closer to the root an exception is located, the more general (abstract) it is. """

# Tree Example
""" ZeroDivisionError => ArithmeticError => Exception => BaseException."""


# ----------- Replacing ZeroDivisionError with ArithmeticError ---------------------------
""" ArithmeticError is a general class including (among others) the ZeroDivisionError exception. 
    This also means that replacing the exception's name with either Exception or BaseException won't 
    change the program's behavior. """

try:
    y = 1 / 0
except ArithmeticError:
    print("Oooppsss...")

print("THE END.")

# -----------------------------------------------------------------------------------------


# ------------------------- Example 2 -----------------------------------------------------

try:
    y = 1 / 0
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:  # unreachable
    print("Zero Division!")

print("THE END.")

# Arithmetic problem!
# THE END.
# -----------------------------------------------------------------------------------------


""" If you want to handle two or more exceptions in the same way, you can use the following syntax: """

# try:
#     :
# except (exc1, exc2):
#     :


""" Note: the exception raised can cross function and module boundaries, and travel through the invocation chain 
looking for a matching except clause able to handle it."""

""" If there is no such clause -  terminates your code and emits a diagnostic message."""


# The raise Instruction
""" The raise instruction raises the specified exception named exc as if it was raised in a normal (natural) way: """

""" The instruction enables you to:
1)  simulate raising actual exceptions (e.g., to test your handling strategy)
2)  partially handle an exception and make another part of the code responsible for completing the 
    handling (separation of concerns)."""

""" There is one serious restriction: this kind of raise instruction may be used inside the except branch only;
    using it in any other context causes an error."""

# ------------------------------------------------------------------------------------------

# Assert

# import math
#
# x = -2
# assert x >= 0.0
#
# x = math.sqrt(x)
#
# print(x)
# # AssertionError

""" How does it work?

1) It evaluates the expression;

2) if the expression evaluates to True, or a non-zero numerical value, or a non-empty string, or any other value
   different than None, it won't do anything else;
   
3) otherwise, it automatically and immediately raises an exception named AssertionError (in this case, we say 
   that the assertion has failed)"""


""" How it can be used?

1)  you may want to put it into your code where you want to be absolutely safe from evidently wrong data, and where
    you aren't absolutely sure that the data has been carefully examined before (inside a function used by someone else)
    
2)  raising an AssertionError exception secures your code from producing invalid results, and clearly shows the nature 
    of the failure;
    
3)  assertions don't supersede exceptions or validate the data - they are their supplements."""


def foo(x):
    assert x
    return 1/x


try:
    print(foo(0))
except ZeroDivisionError:
    print("zero")
except:
    print("for assertion")
    #  for assertion
