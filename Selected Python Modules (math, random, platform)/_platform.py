""" The platform module lets you access the underlying platform's data, i.e., hardware, operating system,
and interpreter version information """

from platform import platform, machine, processor, system, version, python_implementation, python_version_tuple

# print(platform())
# print(platform(1))
# print(platform(0, 1))

""" 
aliased → when set to True (or any non-zero value) it may cause the function
          to present the alternative underlying layer names instead of the common ones;

terse   → when set to True (or any non-zero value) it may convince the function to 
          present a briefer form of the result (if possible)"""
# print(platform(aliased=False, terse=False))
# Linux-*.*.*-****-amd64-x86_64-****.**


"""
 the function machine() will tell you the generic name of the processor
 which runs your OS together with Python and your code

"""

# print(machine())
# x86_64


""" The processor() function returns a string filled with the real processor name (if possible). """
# print(processor())
# nothing printed in our case xD. It may be like Intel(R) Core(TM) i3-2330M CPU @ 2.20GHz


""" A function named system() returns the generic OS name as a string. """
# print(system())
# Linux


""" The OS version is provided as a string by the version() function. """
# print(version())
# #1 SMP PREEMPT Debian 5.16.7-2kali1 (2022-02-10)


""" 
 If you need to know what version of Python is running your code, you can check it using a number of
 dedicated functions - here are two of them:
 
 python_implementation() → returns a string denoting the Python implementation
"""
# print(python_implementation())
# CPython

""" CPython is the reference implementation of the Python programming language. Written in C and Python, CPython is 
the default and most widely used implementation of the Python language. CPython can be defined as both an interpreter 
and a compiler as it compiles Python code into bytecode """


""" 
python_version_tuple() → returns a three-element tuple filled with:
                             the major part of Python's version;
                             the minor part;
                             the patch level number.
"""
# print(python_version_tuple())
# ('3', '9', '10')


""" You can read about all standard Python modules here: https://docs.python.org/3/py-modindex.html."""
