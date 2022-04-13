""" What is Inheritance?

Inheritance is a common practice (in object programming) of passing attributes and methods from the superclass
(defined and existing) to a newly created class, called the subclass.

In other words, inheritance is a way of building a new class, not from scratch, but by using an already defined
repertoire of traits. The new class inherits (and this is the key) all the already existing equipment,
but is able to add some new ones if needed."""


# -------------------- A very simple example of two-level inheritance is presented here: ------------------------------


class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass

# The Vehicle class is the superclass for both the LandVehicle and TrackedVehicle classes;
# The LandVehicle class is a subclass of Vehicle and a superclass of TrackedVehicle at the same time;
# The TrackedVehicle class is a subclass of both the Vehicle and LandVehicle classes.

# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------- issubclass() --------------------------------------------------------------------
""" Inheritance: issubclass() """
# Python offers a function which is able to identify a relationship between two classes,
# and although its diagnosis isn't complex, it can check if a particular class is a subclass of any other class.

""" The function returns True if ClassOne is a subclass of ClassTwo, and False otherwise. """
# issubclass(ClassOne, ClassTwo)

# [!] There is one important observation to make: each class is considered to be a subclass of itself.

print("issubclass() example".center(40, '-'))
for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()

""" 
↓ is a subclass of →	Vehicle	LandVehicle	TrackedVehicle

Vehicle	                True	  False	    False
LandVehicle	            True	  True	    False
TrackedVehicle	        True	  True	    True

"""
# --------------------------------------------------------------------------------------------------------------------


# --------------------------------- isinstance() ---------------------------------------------------------------------

""" Let's assume that you've got a cake (e.g., as an argument passed to your function).
You want to know what recipe has been used to make it. Why? Because you want to know what to expect from it,
e.g., whether it contains nuts or not, which is crucial information to some people."""


""" The functions returns True if the object is an instance of the class, or False otherwise. """
# isinstance(objectName, ClassName)

""" Being an instance of a class means that the object (the cake) has been prepared using a recipe contained in either 
the class or one of its superclasses."""

my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

print("isinstance() example".center(40, '-'))
for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()

""" 
↓ is an instance of →	Vehicle	LandVehicle	TrackedVehicle
my_vehicle	            True	 False	    False
my_land_vehicle	        True	 True	    False
my_tracked_vehicle	    True	 True	    True
"""
# ---------------------------------------------------------------------------------------------------------------------


# ------------------------------------- the is operator --------------------------------------------------------------
""" There is also a Python operator worth mentioning, as it refers directly to objects - here it is: """


""" The is operator checks whether two variables (object_one and object_two here) refer to the same object."""
# object_one is object_two

""" [!] Don't forget that variables don't store the objects themselves, but only the handles pointing 
    to the internal Python memory."""

print("The is operator example".center(40, '-'))


class SampleClass:
    def __init__(self, val):
        self.val = val


object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2)  # False
print(object_2 is object_3)  # False
print(object_3 is object_1)  # True
print(object_1.val, object_2.val, object_3.val)  # 1 2 1

string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"

print(string_1 == string_2, string_1 is string_2)
""" Assigning a value of an object variable to another variable doesn't copy the object, but only its handle. 
This is why an operator like is may be very useful in particular circumstances."""

# ---------------------------------------------------------------------------------------------------------------------


# ------------------------------------- How Python finds properties and methods ---------------------------------------
""" Now we're going to look at how Python deals with inheriting methods.


Take a look at the example below. Let's analyze it:
1)  there is a class named Super, which defines its own constructor used to assign the object's property, named name.

2)  the class defines the __str__() method, too, which makes the class able to present its identity in clear text form.

3)  the class is next used as a base to create a subclass named Sub. The Sub class defines its own constructor, which 
    invokes the one from the superclass. Note how we've done it: Super.__init__(self, name).

4)  we've explicitly named the superclass, and pointed to the method to invoke __init__(), providing all needed 
    arguments. we've instantiated one object of class Sub and printed it."""

print("properties and methods example".center(40, '-'))


class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        # Super.__init__(self, name)  # Second way to call a supper class
        super().__init__(name)
        """ The super() function creates a context in which you don't have to (moreover, you mustn't) 
        pass the self argument to the method being invoked - this is why it's possible to activate the 
        superclass constructor using only one argument."""


obj = Sub("Andy")

print(obj)

""" [!] : you can use this mechanism > "super() " not only to invoke the superclass constructor, but also to get access
 to any of the resources available inside the superclass."""
# ---------------------------------------------------------------------------------------------------------------------


# ----------------------------------- Testing Properties --------------------------------------------------------------

print("Testing Properties".center(40, '-'))


""" The Super class defines one class variable named supVar, and the Sub class defines a variable named subVar."""


class Super:
    supVar = 1


class Sub(Super):
    subVar = 2


obj = Sub()

print(obj.subVar)  # 2
print(obj.supVar)  # 1
"""     [!] Both these variables are visible inside the object of class Sub  """

# ---------------------------------------------------------------------------------------------------------------------


# ----------------------------------- Testing Properties Continued ----------------------------------------------------

""" The Sub class constructor creates an instance variable named subVar, while the Super constructor does the same with
    a variable named supVar. As previously, both variables are accessible from within the object of class Sub."""

print("Testing Properties 2".center(40, '-'))


class Super:
    def __init__(self):
        self.supVar = 11


class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12


obj = Sub()

print(obj.subVar)
print(obj.supVar)

# ---------------------------------------------------------------------------------------------------------------------


# ----------------------------------How Python finds properties and methods: continued---------------------------------
""" When you try to access any object's entity, Python will try to (in this order):

    1)  find it inside the object itself;
    2)  find it in all classes involved in the object's inheritance line from bottom to top

[!] if both of the above fail, an exception (AttributeError) is raised."""

print("Testing Properties 3".center(40, '-'))


class Level1:
    variable_1 = 100

    def __init__(self):
        self.var_1 = 101

    def fun_1(self):
        return 102


class Level2(Level1):
    variable_2 = 200

    def __init__(self):
        super().__init__()
        self.var_2 = 201

    def fun_2(self):
        return 202


class Level3(Level2):
    variable_3 = 300

    def __init__(self):
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 302


obj = Level3()

print(obj.variable_1, obj.var_1, obj.fun_1())  # 100 101 102
print(obj.variable_2, obj.var_2, obj.fun_2())  # 200 201 202
print(obj.variable_3, obj.var_3, obj.fun_3())  # 300 301 302


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------How Python finds properties and methods: continued---------------------------------
print("Testing Properties 4".center(40, '-'))

""" Multiple inheritance occurs when a class has more than one superclass. Syntactically, such inheritance is presented
as a comma-separated list of superclasses put inside parentheses after the new class name - just like here:"""


class SuperA:
    var_a = 10

    def fun_a(self):
        return 11


class SuperB:
    var_b = 20

    def fun_b(self):
        return 21


class Sub(SuperA, SuperB):
    pass


obj = Sub()

print(obj.var_a, obj.fun_a())  # 10 11
print(obj.var_b, obj.fun_b())  # 20 21

""" The Sub class has two superclasses: SuperA and SuperB. This means that the Sub class inherits all the goods 
offered by both SuperA and SuperB. """

""" Now it's time to introduce a brand new term - overriding."""
# ---------------------------------------------------------------------------------------------------------------------


# --------------------------------- How Python finds properties and methods: continued --------------------------------
""" Both, Level1 and Level2 classes define a method named fun() and a property named var. Does this mean that the 
Level3 class object will be able to access two copies of each entity? Not at all.

The entity defined later (in the inheritance sense) overrides the same entity defined earlier. 
This is why the code produces the following output:"""

print("Testing Properties 5".center(40, '-'))


class Level1:
    var = 100

    def fun(self):
        return 101


class Level2(Level1):
    var = 200

    def fun(self):
        return 201


class Level3(Level2):
    pass


obj = Level3()

print(obj.var, obj.fun())   # 200 201

# ---------------------------------------------------------------------------------------------------------------------


# --------------------------------- How Python finds properties and methods: continued --------------------------------

print("Testing Properties 6".center(40, '-'))

""" We can say that Python looks for object components in the following order:

    1) inside the object itself;
    2) in its superclasses, from bottom to top;
    3) if there is more than one class on a particular inheritance path, Python scans them from left to right."""


class Left:
    var = "L"
    var_left = "LL"

    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"

    def fun(self):
        return "Right"


class Sub(Left, Right):
    pass


obj = Sub()

print(obj.var, obj.var_left, obj.var_right, obj.fun())  # L LL RR Left

# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------- How to build a hierarchy of classes ----------------------------------------

print("Hierarchy of classes".center(40, '-'))

class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print("do_it from Two")


one = One()
two = Two()

one.doanything()  # do_it from One
two.doanything()  # do_it from Two"

""" Note: the situation in which the subclass is able to modify its superclass behavior (just like in the example)
is called [!] Polymorphism. The word comes from Greek (polys: "many, much" and morphe, "form, shape"), which means that 
one and the same class can take various forms depending on the redefinitions done by any of its subclasses."""

""" [!] The method, redefined in any of the superclasses, thus changing the behavior of the superclass, 
    [!] is called Virtual. """

# In other words, no class is given once and for all. Each class's behavior may be modified at
# any time by any of its subclasses.

# ---------------------------------------------------------------------------------------------------------------------


# ----------------------------------- How to build a hierarchy of classes: continued ----------------------------------

"""if we are going to put all the details into the subclass (such a method is often called an [!] abstract method """

# Inheritance is not the only way of constructing adaptable classes. You can achieve the same goals
# (not always, but very often) by using a technique named [!] composition.

""" Composition is the process of composing an object using other different objects. The objects used in the
composition deliver a set of desired traits (properties and/or methods) so we can say that they act like blocks
used to build a more complicated structure."""


""" It can be said that:

[!] Inheritance - extends a class's capabilities by adding new components and modifying existing ones; in other words,
the complete recipe is contained inside the class itself and all its ancestors;
the object takes all the class's belongings and makes use of them;


[!] Composition - projects a class as a container able to store and use other objects (derived from other classes) 
where each of the objects implements a part of a desired class's behavior. """

print("Hierarchy of classes 2".center(40, '-'))

import time


class Tracks:
    def change_direction(self, left, on):
        print("tracks: ", left, on)


class Wheels:
    def change_direction(self, left, on):
        print("wheels: ", left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)


wheeled = Vehicle(Wheels())  # Wheels: True True, Wheels: True False
tracked = Vehicle(Tracks())  # Tracks: False True, Tracks: False False

wheeled.turn(True)
tracked.turn(False)

# ---------------------------------------------------------------------------------------------------------------------


# ------------------------------------ Single inheritance vs. multiple inheritance ------------------------------------

""" Don't forget that:

1) a single inheritance class is always simpler, safer, and easier to understand and maintain;

2) multiple inheritance is always risky, as you have many more opportunities to make a mistake in identifying these 
   parts of the superclasses which will effectively influence the new class;

3) multiple inheritance may make overriding extremely tricky; moreover, using the super() function becomes ambiguous;

4) multiple inheritance violates the single responsibility principle 
   (more details here: https://en.wikipedia.org/wiki/Single_responsibility_principle) 
   as it makes a new class of two (or more) classes that know nothing about each other;
   
5) we strongly suggest multiple inheritance as the last of all possible solutions - if you really need the many 
   different functionalities offered by different classes, composition may be a better alternative."""

# ---------------------------------------------------------------------------------------------------------------------


# -------------- What is Method Resolution Order (MRO) and why is it that not all inheritances make sense? -------------

print("1) Method Resolution Order (MRO)".center(40, '-'))


class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Middle):
    def m_bottom(self):
        print("bottom")


my_object = Bottom()
my_object.m_bottom()  # bottom
my_object.m_middle()  # middle
my_object.m_top()     # top


# -------------------------------------- Example 2 MRO ----------------------------------------------------------------
print("2) Method Resolution Order (MRO)".center(40, '-'))

try:
    class Top:
        def m_top(self):
            print("top")


    class Middle(Top):
        def m_middle(self):
            print("middle")


    class Bottom(Top, Middle):
        def m_bottom(self):
            print("bottom")


    new_object = Bottom()
    new_object.m_bottom()  # bottom
    new_object.m_middle()  # middle
    new_object.m_top()     # top

except TypeError:
    print("[!] TypeError: Cannot create a consistent method resolution order (MRO) for bases Top, Middle.")

""" this amendment has spoiled the code, and it won't run anymore. What a pity. The order we tried to force 
    (Top, Middle) is incompatible with the inheritance path which is derived from the code's structure. 
    Python won't like it. """
# ---------------------------------------------------------------------------------------------------------------------


# -------------------------------------------- The diamond problem  ---------------------------------------------------

print("The Diamond Problem".center(40, '-'))


class Top:
    def m_top(self):
        print("top")


class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")


class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")


class Bottom(Middle_Left, Middle_Right):
    def m_bottom(self):
        print("bottom")


diamond_object = Bottom()
diamond_object.m_bottom()  # bottom
diamond_object.m_middle()  # middle_left
diamond_object.m_top()     # top

""" Note: both Middle classes define a method of the same name: m_middle().

It introduces a small uncertainty to our sample, although we're absolutely sure that you can answer the following 
key question: which of the two m_middle() methods will actually be invoked when the following line is executed? """

# ---------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------- Key Takeaways ---------------------------------------------------

""" 1. A method named __str__() is responsible for converting an object's contents into a (more or less) readable
string. You can redefine it if you want your object to be able to present itself in a more elegant form. For example:"""

print("1) Key Takeaways".center(40, '-'))


class Mouse:
    def __init__(self, name):
        self.my_name = name

    def __str__(self):
        return self.my_name


the_mouse = Mouse('mickey')
print(the_mouse)  # Prints "mickey".

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

""" 2. A function named issubclass(Class_1, Class_2) is able to determine if Class_1 is a subclass of Class_2."""
print("2) Key Takeaways".center(40, '-'))


class Mouse:
    pass


class LabMouse(Mouse):
    pass


print(issubclass(Mouse, LabMouse), issubclass(LabMouse, Mouse))  # Prints "False True"

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

""" 3. A function named isinstance(Object, Class) checks if an object comes from an indicated class. For example: """

print("3) Key Takeaways".center(40, '-'))


class Mouse:
    pass


class LabMouse(Mouse):
    pass


mickey = Mouse()
print(isinstance(mickey, Mouse), isinstance(mickey, LabMouse))  # Prints "True False".

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

""" 4. A operator called is checks if two variables refer to the same object. For example: """

print("4) Key Takeaways".center(40, '-'))


class Mouse:
    pass


mickey = Mouse()
minnie = Mouse()
cloned_mickey = mickey
print(mickey is minnie, mickey is cloned_mickey)  # Prints "False True".
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

""" 5. A parameterless function named super() returns a reference to the nearest superclass of the class."""

print("5) Key Takeaways".center(40, '-'))


class Mouse:
    def __str__(self):
        return "Mouse"


class LabMouse(Mouse):
    def __str__(self):
        return "Laboratory " + super().__str__()


doctor_mouse = LabMouse()
print(doctor_mouse)  # Prints "Laboratory Mouse".
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

""" 6.  Methods as well as instance and class variables defined in a superclass are automatically inherited by 
        their subclasses. For example:"""

print("6) Key Takeaways".center(40, '-'))


class Mouse:
    Population = 0

    def __init__(self, name):
        Mouse.Population += 1
        self.name = name

    def __str__(self):
        return "Hi, my name is " + self.name


class LabMouse(Mouse):
    pass


professor_mouse = LabMouse("Professor Mouser")
print(professor_mouse, Mouse.Population)  # Prints "Hi, my name is Professor Mouser 1"
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

""" 7. In order to find any object/class property, Python looks for it inside:

    1) the object itself;
    2) all classes involved in the object's inheritance line from bottom to top;
    3) if there is more than one class on a particular inheritance path, Python scans them from left to right;
    4) if both of the above fail, the AttributeError exception is raised. """

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

""" 8. If any of the subclasses defines a method/class variable/instance variable of the same name as existing in 
the superclass, the new name overrides any of the previous instances of the name. For example:"""

print("8) Key Takeaways".center(40, '-'))


class Mouse:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name


class AncientMouse(Mouse):
    def __str__(self):
        return "Meum nomen est " + self.name


mus = AncientMouse("Caesar")  # Prints "Meum nomen est Caesar"
print(mus)
# True False
# 2