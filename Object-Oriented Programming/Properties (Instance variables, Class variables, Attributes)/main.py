""" Python objects, when created, are gifted with a small set of predefined properties and methods. Each object has
got them, whether you want them or not. One of them is a variable named [!] __dict__ (it's a dictionary).
The variable contains the names and values of all the properties (variables) the object is currently carrying."""


# ------------------------------------ Example 1 ----------------------------------------------------------------------


class ExampleClass:
    def __init__(self, val=1):
        self.first = val

    def set_second(self, val):
        self.second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5  # third property is not defined in the class, but it's fully permissible

print(example_object_1.__dict__)  # {'first': 1}
print(example_object_2.__dict__)  # {'first': 2, 'second': 3}
print(example_object_3.__dict__)  # {'first': 4, 'third': 5}

print("End of Example 1".center(40, '-'))


# ---------------------------------------------------------------------------------------------------------------------

# [!] modifying an instance variable of any object has no impact on all the remaining objects.
# [!] Instance variables are perfectly isolated from each other.


# ------------------------------------ Example 2 ----------------------------------------------------------------------

class NewExampleClass:
    def __init__(self, val=1):
        self.__first = val  # private

    def set_second(self, val=2):
        self.__second = val  # private


example_object_1 = NewExampleClass()
example_object_2 = NewExampleClass(2)

example_object_2.set_second(3)

example_object_3 = NewExampleClass(4)
example_object_3.__third = 5  # This is not also defined in Class itself, but it is fully permissible too

print(example_object_1.__dict__)  # {'_NewExampleClass__first': 1}
print(example_object_2.__dict__)  # {'_NewExampleClass__first': 2, '_NewExampleClass__second': 3}
print(example_object_3.__dict__)  # {'_NewExampleClass__first': 4, '__third': 5}

print("End of Example 2".center(40, '-'))


# ---------------------------------------------------------------------------------------------------------------------


# ------------------------------------ Example 3 ----------------------------------------------------------------------
class MyExampleClass:
    """ in effect, the variable counts all the created objects.

    class variables aren't shown in an object's __dict__ (this is natural as class variables aren't parts of an object)
    but you can always try to look into the variable of the same name, but at the class level.

    a class variable always presents the same value in all class instances (objects)"""
    counter = 0  # outside any of its methods makes the variable a class variable.

    def __init__(self, val=1):
        self.__first = val
        MyExampleClass.counter += 1


example_object_1 = MyExampleClass()
example_object_2 = MyExampleClass(2)
example_object_3 = MyExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)  # {'_MyExampleClass__first': 1} 3
print(example_object_2.__dict__, example_object_2.counter)  # {'_MyExampleClass__first': 2} 3
print(example_object_3.__dict__, example_object_3.counter)  # {'_MyExampleClass__first': 4} 3

print("End of Example 3".center(40, '-'))


# ---------------------------------------------------------------------------------------------------------------------


# ------------------------------------ Example 4 ----------------------------------------------------------------------
class SomeExampleClass:
    __counter = 0

    def __init__(self, val=1):
        self.__first = val
        SomeExampleClass.__counter += 1


example_object_1 = SomeExampleClass()
example_object_2 = SomeExampleClass(2)
example_object_3 = SomeExampleClass(4)

print(example_object_1.__dict__, example_object_1._SomeExampleClass__counter)  # {'_SomeExampleClass__first': 1} 3
print(example_object_2.__dict__, example_object_2._SomeExampleClass__counter)  # {'_SomeExampleClass__first': 2} 3
print(example_object_3.__dict__, example_object_3._SomeExampleClass__counter)  # {'_SomeExampleClass__first': 4} 3

print("End of Example 4".center(40, '-'))
# ---------------------------------------------------------------------------------------------------------------------


# ------------------------------------ Example 5 ----------------------------------------------------------------------
class CoolExampleClass:
    varia = 1

    def __init__(self, val):
        CoolExampleClass.varia = val


print(CoolExampleClass.__dict__)  # ... 'varia': 1, ...
example_object = CoolExampleClass(2)

print(CoolExampleClass.__dict__) # ... 'varia': 2, ...
print(example_object.__dict__)  # Note that the object's __dict__ is empty - the object has no instance variables.

print("End of Example 5".center(40, '-'))
# ---------------------------------------------------------------------------------------------------------------------


# ------------------------------------ Example 6 ----------------------------------------------------------------------

""" Python provides a function which is able to safely check if any object/class contains a specified property. 
The function is named hasattr, and expects two arguments to be passed to it:

1)  the class or the object being checked;
2)  the name of the property whose existence has to be reported (note: it has to be a string containing the attribute
    name, not the name alone) 
    
The function (hasattr) returns True or False. """


class AttributeExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = AttributeExampleClass(1)
print(example_object.a)  # 1

""" [!] using hasattr function """
if hasattr(example_object, 'b'):  # False
    print(example_object.b)

print("End of Example 6".center(40, '-'))
# ---------------------------------------------------------------------------------------------------------------------


# ------------------------------------ Example 7 ----------------------------------------------------------------------
""" Don't forget that the hasattr() function can operate on classes, too. You can use it to find out if a class
    variable is available, just like here in the example in the editor.

    The function returns True if the specified class contains a given attribute, and False otherwise."""


class SimpleExampleClass:
    attr = 1


print(hasattr(SimpleExampleClass, 'attr'))  # True
print(hasattr(SimpleExampleClass, 'prop'))  # False

print("End of Example 7".center(40, '-'))
# ---------------------------------------------------------------------------------------------------------------------


# ------------------------------------------ Key Takeaways ------------------------------------------------------------
""" 1.  An instance variable is a property whose existence depends on the creation of an object. Every object can have
        a different set of instance variables.
        
        Moreover, they can be freely added to and removed from objects during their lifetime. All object instance 
        variables are stored inside a dedicated dictionary named __dict__, contained in every object separately. """


""" 2.  An instance variable can be private when its name starts with __, but don't forget that such a property is 
        still accessible from outside the class using a mangled name constructed as _ClassName__PrivatePropertyName."""


""" 3.  A class variable is a property which exists in exactly one copy, and doesn't need any created object to be
        accessible. Such variables are not shown as __dict__ content. 
        
        All a class's class variables are stored inside a dedicated dictionary named __dict__, contained in 
        every class separately. """


""" 4.  A function named hasattr() can be used to determine if any object/class contains a specified property."""
# ---------------------------------------------------------------------------------------------------------------------
