# The capitalize() method
print("Alpha".capitalize())  # Alpha
print('ALPHA'.capitalize())  # Alpha
print(' Alpha'.capitalize())  # ' alpha'
print('123'.capitalize())  # 123
print("αβγδ".capitalize())  # Αβγδ


# The center() method
print('[' + 'Beta'.center(2) + ']')  # [Beta]
print('[' + 'Beta'.center(20) + ']')  # [        Beta        ]
print('[' + 'gamma'.center(20, '*') + ']')  # [*******gamma********]


# The endswith() method
t = "zeta"
print(t.endswith("a"))  # True
print(t.endswith("eta"))  # True


# The startswith() method
""" The startswith() method is a mirror reflection of endswith() - it checks if a given string starts with
the specified substring."""

print("omega".startswith("meg"))  # False
print("omega".startswith("om"))  # True

# The find() method
""" The find() method is similar to index(), which you already know - it looks for a substring and returns the index 
of first occurrence of this substring, but: 

1)it's safer - it doesn't generate an error for an argument containing a non-existent substring (it returns -1 then).
2)it works with strings only - don't try to apply it to any other sequence."""

print("Eta".find("ta"))  # 1
print("Eta".find("mma"))  # -1

""" If you want to perform the find, not from the string's beginning, but from any position, you can use a 
two-parameter variant of the find() method. Look at the example 

The second argument specifies the index at which the search will be started (it doesn't have to fit inside the string).
"""
print('kappa'.find('a', 2))  # 4

# find() method example:
the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)  # 15 80 198 221 238
    fnd = the_text.find('the', fnd + 1)
# end of example

""" There is also a three-parameter mutation of the find() method - the third argument points to the first index which
 won't be taken into consideration during the search (it's actually the upper limit of the search)."""
print('kappa'.find('a', 1, 4))  # 1
print('kappa'.find('a', 2, 4))  # -1
print('saqartveloa'.find("a", 2, 11))  # 3


# The rfind() method
""" The one-, two-, and three-parameter methods named rfind() do nearly the same things as their counterparts (the 
ones devoid of the r prefix), but start their searches from the end of the string, not the beginning (hence the 
prefix r, for right). """

print("tau tau tau".rfind("ta"))  # 8
print("tau tau tau".rfind("ta", 9))  # -1
print("tau tau tau".rfind("ta", 3, 9))  # 4


# The isalnum() method
""" The parameterless method named isalnum() checks if the string contains only digits or alphabetical characters (
letters), and returns True or False according to the result. """
print('lambda30'.isalnum())  # True
print('lambda'.isalnum())  # True
print('30'.isalnum())  # True
print('@'.isalnum())  # False
print('lambda_30'.isalnum())  # False
print(''.isalnum())  # False

t = 'Six lambdas'
print(t.isalnum())  # False (the cause of the result is a space - it's neither a digit nor a letter)

# The isalpha() method
""" The isalpha() method is more specialized - it's interested in letters only. """

print("Moooo".isalpha())  # True
print('Mu40'.isalpha())  # False


# The isdigit() method
""" In turn, the isdigit() method looks at digits only - anything else produces False as the result """

print('2018'.isdigit())  # True
print("Year2019".isdigit())  # False


# The islower() method
""" The islower() method is a fussy variant of isalpha() - it accepts lower-case letters only. """

print("Moooo".islower())  # False
print('moooo'.islower())  # True


# The isspace() method
"""The isspace() method identifies whitespaces only - it disregards any other character (the result is False then)."""

print(' \n '.isspace())  # True
print(" ".isspace())  # True
print("mooo mooo mooo".isspace())  # False


# The isupper() method
""" The isupper() method is the upper-case version of islower() - it concentrates on upper-case letters only. """
print("Moooo".isupper())  # False
print('moooo'.isupper())  # False
print('MOOOO'.isupper())  # True


# The join() method
""" The join() method is rather complicated, so let us guide you step by step thorough it:

1)as its name suggests, the method performs a join - it expects one argument as a list; it must be assured that all the 
list's elements are strings - the method will raise a TypeError exception otherwise; 

2)all the list's elements will be joined into one string but... ...the string from which the method has been invoked 
is used as a separator, put among the strings; 

3)the newly created string is returned as a result. """

print(",".join(["omicron", "pi", "rho"]))  # omicron,pi,rho


# The lower() method
""" The lower() method makes a copy of a source string, replaces all upper-case letters with their lower-case 
counterparts, and returns the string as the result. Again, the source string remains untouched. """

print("SiGmA=60".lower())  # sigma=60


# The lstrip() method
""" (Note: left strip) The parameterless lstrip() method returns a newly created string formed from the original one by 
removing all leading whitespaces. """

print("www.cisco.com".lstrip("w."))  # cisco.com

print("pythoninstitute.org".lstrip(".org"))  # pythoninstitute.org (nothing changed,cuz neither ./o/r/g found from left)

print("[" + " tau ".lstrip() + "]")  # [tau ]

print("zoro.org".lstrip('zoro.'))  # g

print("monkey.mo".lstrip('mo'))  # nkey.mo


# The rstrip() method
""" Two variants of the rstrip() method do nearly the same as lstrips, but affect the opposite side of the string. """

print("[" + " upsilon ".rstrip() + "]")  # [ upilson]
print("cisco.com".rstrip(".com"))  # cis


# The strip() method
""" The strip() method combines the effects caused by rstrip() and lstrip() - it makes a new string lacking all the
leading and trailing whitespaces."""

print("[" + "   aleph   ".strip() + "]")  # [aleph]


# The split() method
""" The split() method does what it says - it splits the string and builds a list of all detected substrings. 

The method assumes that the substrings are delimited by whitespaces - the spaces don't take part in the operation,
and aren't copied into the resulting list."""

print("phi       chi\npsi".split())  # ['phi', 'chi', 'psi']


# The replace() method
""" The two-parameter replace() method returns a copy of the original string in which all occurrences of the first 
argument have been replaced by the second argument. """

print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))  # www.pythoninstitute.org
print("This is it!".replace("is", "are"))  # Thare are it!


""" The three-parameter replace() variant uses the third argument (a number) to limit the number of replacements."""

print("This is it!".replace("is", "are", 1))  # Thare is it


# The swapcase() method
""" The swapcase() method makes a new string by swapping the case of all letters within the source string:
lower-case characters become upper-case, and vice versa.

All other characters remain untouched."""

print("I know that I know nothing.".swapcase())  # i KNOW THAT i KNOW NOTHING.


# The title() method
""" The title() method performs a somewhat similar function - it changes every word's first letter to upper-case, 
turning all other ones to lower-case."""

print("I know that I know nothing. Part 1.".title())  # I Know That I Know Nothing. Part 1.


# The upper() method
""" Last but not least, the upper() method makes a copy of the source string, replaces all lower-case letters with
their upper-case counterparts, and returns the string as the result."""

print("I know that I know nothing. Part 2.".upper())  # I KNOW THAT I KNOW NOTHING. PART 2.
