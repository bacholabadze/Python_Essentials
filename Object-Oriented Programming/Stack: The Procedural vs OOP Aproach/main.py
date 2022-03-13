""" What is a stack? - A stack is a structure developed to store data in a very specific way."""

# Imagine a stack of coins. You aren't able to put a coin anywhere else but on the top of the stack.
# Similarly, you can't get a coin off the stack from any place other than the top of the stack.
# If you want to get the coin that lies on the bottom, you have to remove all the coins from the higher levels.


""" The alternative name for a stack (but only in IT terminology) is [!] LIFO. (Last In - First Out) """
# A stack is an object with two elementary operations, conventionally named push (when a new element is put on the top)
# and pop (when an existing element is taken away from the top).

# ----------------------------------------------- Stack Example #1 ----------------------------------------------------
stack = []


def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]
    return val


push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())
print('END OF EXAMPLE 1'.center(40, '-'))
# ---------------------------------------------------------------------------------------------------------------------


""" he objective approach delivers solutions for each of the above problems. Let's name them first:

1) the ability to hide (protect) selected values against unauthorized access is called [!]encapsulation;
the encapsulated values can be neither accessed nor modified if you want to use them exclusively;

2) when you have a class implementing all the needed stack behaviors, you can produce as many stacks as you want;
you needn't copy or replicate any part of the code;

3) the ability to enrich the stack with new functions comes from inheritance; you can create a new class (a subclass)
which inherits all the existing traits from the superclass, and adds some new ones.
"""


# --------------------------------- Stack Example 2, OOP approach -----------------------------------------------------


class Stack:
    def __init__(self):
        self.__stack_list = []  # When any class component has a name starting with two underscores (__),
        # it becomes private - this means that it can be accessed only from within the class.


my_stack_object = Stack()
# print(len(my_stack_object.__stack_list))  # AttributeError: 'Stack' object has no attribute '__stack_list'

# ---------------------------------------------------------------------------------------------------------------------


# --------------------------------- Stack Example 3, OOP approach -----------------------------------------------------
class NewStack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object = NewStack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())
print('END OF EXAMPLE 3'.center(40, '-'))
# ---------------------------------------------------------------------------------------------------------------------


# --------------------------------- Stack Example 4, Adding Stack, OOP approach ---------------------------------------
class NewestStack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val


class AddingStack(NewestStack):
    def __init__(self):
        NewestStack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        NewestStack.push(self, val)

    def pop(self):
        val = NewestStack.pop(self)
        self.__sum -= val
        return val


my_latest_stack_object = AddingStack()

for i in range(5):
    my_latest_stack_object.push(i)

print('Sum = ', my_latest_stack_object.get_sum())

for i in range(5):
    print(my_latest_stack_object.pop())
print('END OF EXAMPLE 4'.center(40, '-'))
# ---------------------------------------------------------------------------------------------------------------------

# Enter code here.