"""
Estimated time
15-30 min

Level of difficulty
Easy

Objectives
improving the student's skills in interacting with the operating system;
practical use of known functions provided by the os module.
Scenario
It goes without saying that operating systems allow you to search for files and directories.
While studying this part of the course, you learned about the functions of the os module, which have
everything you need to write a program that will search for directories in a given location.

To make your task easier, we have prepared a test directory structure for you:"""

import os

# print(os.getcwd())


def find(path, mydir):
    try:
        os.chdir(path)
    except OSError:
        # print("Doesn't process a file that is not a directory")
        return

    current_dir = os.getcwd()
    for entry in os.listdir('.'):
        if mydir in entry:
            print(os.getcwd() + '/' + mydir)
        find(current_dir + '/' + entry, mydir)


find('../', 'python')
