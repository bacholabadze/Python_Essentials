print("Will I be printed in main when called? -Yes!")

# print(__name__)  # 'module' if a file is imported as a module, or __main__ if it's executed directly


""" 
 Personal/Private variable.
 
 Unlike many other programming languages, Python has no means of allowing you to hide such variables 
 from the eyes of the module's users.

 You can only inform your users that this is your variable, that they may read it, 
 but that they should not modify it under any circumstances.

 This is done by preceding the variable's name with _ (one underscore) or __ (two underscores),
 but remember, it's only a convention. Your module's users may obey it or they may no
"""
__counter = 0


def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list):
    global __counter
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod


"""  
 the functions defined inside the module (suml() and prodl()) are available for import;
 we've used the __name__ variable to detect when the file is run stand-alone, and seized this
 opportunity to perform some simple tests 
"""
if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)


""" 
 #! /usr/bin/env python3
 
 the line starting with { #! }  has many names - it may be called shabang, shebang, hashbang, poundbang or
 even hashpling (don't ask us why). The name itself means nothing here - its role is more important.
 
 From Python's point of view, it's just a comment as it starts with #. For Unix and Unix-like OSs 
 (including MacOS) such a line instructs the OS how to execute the contents of the file (in other
 words, what program needs to be launched to interpret the text).

 In some environments (especially those connected with web servers) the absence of that line will cause trouble;
 
 a string (maybe a multiline) placed before any module instructions (including imports) is called
 the doc-string, and should briefly explain the purpose and contents of the module;
"""