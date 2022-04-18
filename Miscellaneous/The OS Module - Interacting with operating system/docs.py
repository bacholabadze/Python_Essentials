""" the os module """

""" In addition to file and directory operations, the os module enables you to:

get information about the operating system;
manage processes;
operate on I/O streams using file descriptors.
"""

# ----------------------------------- Getting information about the operating system -----------------------------------

""" Before you create your first directory structure, you'll see how you can get information about the current 
operating system. This is really easy because the os module provides a function called uname, which returns 
an object containing the following attributes:

        1)systemname — stores the name of the operating system;
        2)nodename — stores the machine name on the network;
        3)release — stores the operating system release;
        4)version — stores the operating system version;
        5)machine — stores the hardware identifier, e.g., x86_64. """

print("Getting information about the operating system".center(60, '-'))

import os
print(os.uname())

# Unfortunately, the uname function only works on some Unix systems.
# If you use Windows, you can use the uname function in the platform module, which returns a similar result.

""" The os module allows you to quickly distinguish the operating system using the name attribute, 
which supports one of the following names:

        posix — you'll get this name if you use Unix;
        nt — you'll get this name if you use Windows;
        java — you'll get this name if your code is written in Jython."""

print(os.name)

# NOTE: On Unix systems, there's a command called uname that returns the same information
# (if you run it with the -a option) as the uname function.

# ---------------------------------------------------------------------------------------------------------------------

# ------------------------------------------- Creating directories in Python -------------------------------------------
""" The os module provides a function called mkdir, which, like the mkdir command in Unix and Windows, allows you to 
create a directory. The mkdir function requires a path that can be relative or absolute. 
Let's recall what both paths look like in practice:

        my_first_directory —    this is a relative path which will create the my_first_directory
                                directory in the current working directory;
        
        ./my_first_directory —  this is a relative path that explicitly points to the current working
                                directory. It has the same effect as the path above;
        
        ../my_first_directory — this is a relative path that will create the my_first_directory 
                                directory in the parent directory of the current working directory;

        /python/my_first_directory — this is the absolute path that will create the my_first_directory 
                                     directory, which in turn is in the python directory in the root directory."""

print("Creating directories in Python".center(60, '-'))
import os

try:
    os.mkdir("My Test Directory")  # Note that running the program twice will raise a FileExistsError.
except FileExistsError:
    print("File Already Exists")

# Returns a list containing the names of the files and directories that are in the path passed as an argument.
print(os.listdir())

""" This means that we cannot create a directory if it already exists. In addition to the path argument, 
the mkdir function can optionally take the mode argument, which specifies directory permissions. 
However, on some systems, the mode argument is ignored. """

# ---------------------------------------------------------------------------------------------------------------------


# ------------------------------------------- Recursive directory creation -------------------------------------------

""" The mkdir function is very useful, but what if you need to create another directory in the directory 
you've just created. Of course, you can go to the created directory and create another directory inside 
it, but fortunately the os module provides a function called makedirs, which makes this task easier. """

# The makedirs function enables recursive directory creation, which means that all directories in the path will
# be created. Let's look at the code in the editor and see how it is in practice.

print("Recursive directory creation".center(60, '-'))


import os

""" The code creates two directories. The first of them is created in the current working directory, 
while the second in the My Test Directory directory."""

try:
    os.makedirs("My Test Directory/My Second Test Directory")
except FileExistsError:
    print("File Already Exists")


""" To move between directories, you can use a function called chdir, which changes the 
current working directory to the specified path. As an argument, it takes any relative or 
absolute path. In our example, we pass the first directory name to it."""

os.chdir("My Test Directory")

print(os.listdir())

""" NOTE: The equivalent of the makedirs function on Unix systems is the mkdir command with the -p flag, 
while in Windows, simply the mkdir command with the path:

        Unix-like systems:
        
        mkdir -p my_first_directory/my_second_directory
        
        Windows:
        
        mkdir my_first_directory/my_second_directory """

# ---------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------- Where am I now? --------------------------------------------------

""" the os module provides a function that returns information about the current working directory. 
It's called getcwd. Look at the code in the editor to see how to use it in practice."""

# NOTE: On Unix-like systems, the equivalent of the getcwd function is the pwd command,
# which prints the name of the current working directory.

print("Where am I now?".center(60, '-'))

import os

try:
    os.makedirs("my_first_directory/my_second_directory")
except FileExistsError:
    print("File Already Exists")

os.chdir("my_first_directory")
print(os.getcwd())
os.chdir("my_second_directory")
print(os.getcwd())

# ---------------------------------------------------------------------------------------------------------------------


# ------------------------------------------- Deleting directories in Python -------------------------------------------

""" To delete a single directory, you can use a function called rmdir, which takes the path as its argument. """


""" To remove a directory and its subdirectories, you can use the removedirs function, which requires you to 
specify a path containing all directories that should be removed: """

print("Deleting directories in Python".center(60, '-'))

import os

try:
    os.makedirs("my_directory/my_directory")
except FileExistsError:
    print("File Already Exists")
try:
    os.removedirs("my_directory/my_second_directory")
except FileNotFoundError:
    print("File Not Found")

print(os.listdir())

""" As with the rmdir function, if one of the directories doesn't exist or isn't empty, an exception will be raised.

NOTE: In both Windows and Unix, there's a command called rmdir, which, just like the rmdir function, 
removes directories. What's more, both systems have commands to delete a directory and its contents. 
In Unix, this is the rm command with the -r flag. """

# ---------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------- The system() function -----------------------------------------------

""" All functions presented in this part of the course can be replaced by a function called system,
which executes a command passed to it as a string.

The system function is available in both Windows and Unix. Depending on the system, it returns a different result."""

print("The system() function".center(60, '-'))

import os

os.chdir("/home/ambri/Desktop/GITA/Python Essentials/Miscellaneous/The OS Module - Interacting with operating system/")


returned_value = os.system("mkdir my_directory_sys")
print(returned_value)  # we receive exit status 0, which indicates success on Unix systems.

# ---------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------- Key Takeaways ---------------------------------------------------

""" 1. The uname function returns an object that contains information about the current operating system. 
The object has the following attributes:

        systemname (stores the name of the operating system)
        nodename (stores the machine name on the network)
        release (stores the operating system release)
        version (stores the operating system version)
        machine (stores the hardware identifier, e.g. x86_64.) """


""" 2. The name attribute available in the os module allows you to distinguish the operating system. 
It returns one of the following three values:

        posix (you'll get this name if you use Unix)
        nt (you'll get this name if you use Windows)
        java (you'll get this name if your code is written in something like Jython)"""


""" 3. The mkdir function creates a directory in the path passed as its argument. 
The path can be either relative or absolute, e.g: """

# import os
#
# os.mkdir("hello") # the relative path
# os.mkdir("/home/python/hello") # the absolute path

""" Note: If the directory exists, a FileExistsError exception will be thrown. In addition to the mkdir function, 
the os module provides the makedirs function, which allows you to recursively create all directories in a path."""


""" 4. The result of the listdir() function is a list containing the names of the files and 
directories that are in the path passed as its argument.

It's important to remember that the listdir function omits the entries '.' and '..', which are displayed, for example, 
when using the ls -a command on Unix systems. If the path isn't passed, the result will be returned 
for the current working directory. """


""" 5. To move between directories, you can use a function called chdir(), which changes the current working directory 
to the specified path. As its argument, it takes any relative or absolute path.

If you want to find out what the current working directory is, you can use the getcwd() function, which returns 
the path to it. """


""" 6. To remove a directory, you can use the rmdir() function, but to remove a directory and 
its subdirectories, use the removedirs() function."""


""" 7. On both Unix and Windows, you can use the system function, which executes a command 
passed to it as a string, e.g.: """

# import os

# returned_value = os.system("mkdir hello")

""" The system function on Windows returns the value returned by shell after running the command given, while on 
Unix it returns the exit status of the process. """