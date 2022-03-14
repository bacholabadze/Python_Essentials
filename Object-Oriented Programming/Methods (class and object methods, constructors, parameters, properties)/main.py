""" The self parameter is used to obtain access to the object's instance and class variables. """

# ------------------------------------ Example 1 ----------------------------------------------------------------------


class Classy:
    varia = 2

    def method(self):
        print(self.varia, self.var)  # self.var is not defined in class, but after creating it will be (line 14)


obj = Classy()
obj.var = 3
obj.method()

print("End of Example 1".center(40, '-'))
# ---------------------------------------------------------------------------------------------------------------------


# ------------------------------------ Example 2 ----------------------------------------------------------------------

class MoreClassy:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()  # Invokes method named other


obj = MoreClassy()
obj.method()

print("End of Example 2".center(40, '-'))
# ---------------------------------------------------------------------------------------------------------------------

""" If you name a method like this: __init__, it won't be a regular method - it will be a constructor. """


""" If a class has a constructor, it is invoked automatically and implicitly when the object of the
    class is instantiated.

The constructor:

    is obliged to have the self parameter (it's set automatically, as usual);
    
    may (but doesn't need to) have more parameters than just self; if this happens, the way in which the class name
    is used to create the object must reflect the __init__ definition;
    
    can be used to set up the object, i.e., properly initialize its internal state, create instance variables,
    instantiate any other objects if their existence is needed, etc."""


# ------------------------------------ Example 3 ----------------------------------------------------------------------
class LessClassy:
    def __init__(self, value):
        self.var = value


obj_1 = LessClassy("object")

print(obj_1.var)  # object

print("End of Example 3".center(40, '-'))
# ---------------------------------------------------------------------------------------------------------------------

# ------------------------------------ Example 4 ----------------------------------------------------------------------

# a method whose name starts with __ is (partially) hidden.


class MyClassy:
    def visible(self):
        print("visible")

    def __hidden(self):
        print("hidden")


obj = MyClassy()
obj.visible()  # Prints 'visible'

try:
    obj.__hidden()
except:
    print("failed")  # Prints 'failed'

obj._MyClassy__hidden()  # Prints 'hidden'

print("End of Example 4".center(40, '-'))
# ---------------------------------------------------------------------------------------------------------------------


# ------------------------------------ Example 5 ----------------------------------------------------------------------
""" __dict__ is a dictionary. Another built-in property worth mentioning is __name__, which is a string. """


class OfcClassy:
    pass


print(OfcClassy.__name__)  # OfcClassy
obj = OfcClassy()
print(type(obj).__name__)  # OfcClassy


""" Note that a statement like this one:

print(obj.__name__)

will cause an error [!]
"""

print("End of Example 5".center(40, '-'))
# ---------------------------------------------------------------------------------------------------------------------


# ------------------------------------ Example 6 ----------------------------------------------------------------------

""" __module__ is a string, too - it stores the name of the module which contains the definition of the class. """


class TrueClassy:
    pass


print(TrueClassy.__module__)  # __main__
obj = TrueClassy()
print(obj.__module__)  # __main__

""" any module named __main__ is actually not a module, but the file currently being run. """

print("End of Example 6".center(40, '-'))
# ---------------------------------------------------------------------------------------------------------------------

""" __bases__ is a tuple. The tuple contains classes (not class names) which are direct superclasses for the class.

The order is the same as that used inside the class definition """

# Note: only classes have this attribute - objects don't.


# ------------------------------------ Example 7 ----------------------------------------------------------------------


class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)  # ( object )
printBases(SuperTwo)  # ( object )
printBases(Sub)  # ( SuperOne SuperTwo )

# Note: a class without explicit superclasses points to object (a predefined Python class) as its direct ancestor.

print("End of Example 7".center(40, '-'))
# ---------------------------------------------------------------------------------------------------------------------

# Reflection and introspection

""" introspection -> which is the ability of a program to examine the type or properties of an object at runtime  """

""" reflection ->   which goes a step further, and is the ability of a program to manipulate the values, properties
                    and/or functions of an object at runtime."""

# Both reflection and introspection enable a programmer to do anything with every object, no matter where it comes from.


# ------------------------------------ Example 8 ----------------------------------------------------------------------


class MyAwesomeClass:
    pass


obj = MyAwesomeClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


""" The function named incIntsI() gets an object of any class, scans its contents in order to find all integer 
attributes with names starting with i, and increments them by one. """


def incIntsI(obj):
    for name in obj.__dict__.keys():  # scan the __dict__ attribute, looking for all attribute names;
        if name.startswith('i'):  # if a name starts with i
            val = getattr(obj, name)  # Use the getattr() function to get its current value
            if isinstance(val, int):  # Check if the value is of type integer
                setattr(obj, name, val + 1)  # increment the property's value by making use of the setattr() function


print('Before : ')
print(obj.__dict__)

incIntsI(obj)

print("After : ")
print(obj.__dict__)

print("End of Example 8".center(40, '-'))
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------Key Takeaways-----------------------------------------------------------------

""" 1.  A method is a function embedded inside a class. The first (or only) parameter of each method is usually named 
        self, which is designed to identify the object for which the method is invoked in order to access the object's 
        properties or invoke its methods. """


""" 2.  If a class contains a constructor (a method named __init__) it cannot return any value and cannot be 
        invoked directly. """


""" 3.  All classes (but not objects) contain a property named __name__, which stores the name of the class. 
        Additionally, a property named __module__ stores the name of the module in which the class has been declared,
        while the property named __bases__ is a tuple containing a class's superclasses. """

