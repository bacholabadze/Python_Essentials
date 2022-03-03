from sys import path

""" 
 we've used the append() method - in effect, the new path will occupy the last element in the path list;
 if you don't like the idea, you can use insert() instead. 
"""
path.append('..\\modules')


""" When a module is imported, its content is implicitly executed by Python. 
It gives the module the chance to initialize some of its 
internal aspects (e.g., it may assign some variables with useful values).
"""

# zeroes = [i for i in range(5)]
# ones = [i for i in range(1, 5)]
# print(suml(zeroes))  # 10
# print(prodl(ones))  # 24


for p in path:
    print(p)
    # / home / username / Desktop / GITA / Python
    # Essentials / Modules and Packages
    # / home / username / Desktop / GITA / Python / python36.zip
    # ...

""" 
 Note once again: there is a ZIP file listed as one of the path's elements - it's not an error. 
 Python is able to treat zip files as ordinary folders - this can save lots of storage.
"""
