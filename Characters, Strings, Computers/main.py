""" [!] First of all, Python's strings are immutable sequences."""

multiline = '''A
B'''

print(len(multiline))  # prints 3 because of \n

# Operations on strings
str1 = 'a'
str2 = 'b'

print(str1 + str2)  # ab
print(str2 + str1)  # ba
print(5 * 'a')  # aaaaa
print('b' * 4)  # bbbb

""" If you want to know a specific character's ASCII/UNICODE code point value, you can use a
function named ord() (as in ordinal)."""

char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))  # 97
print(ord(char_2))  # 32

""" If you know the code point (number) and want to get the corresponding character,
you can use a function named chr()."""

print(chr(97))  # a
print(chr(945))  # α

# Slicing

alpha = "abdefg"

print(alpha[1:3])  # bd (third index not included)

# in and not in operator

print("a" in alpha)  # True
print("z" not in alpha)  # True

# Operations on strings: min()
print(min("aAbByYzZ"))  # A (cuz it has lowest char code)
print(min([0, 1, 2]))  # 0

# max()
print(max("aAbByYzZ"))  # z
print(max([0, 1, 2]))  # 2

# Operations on strings: the index() method
""" The method returns the index of the first occurrence of the argument """

print("aAbByYzZaA".index("b"))  # 2
print("aAbByYzZaA".index("Z"))  # 7


# Operations on strings: the list() function
""" The list() function takes its argument (a string) and creates a new list containing all the string's characters, 
one per list element. """

print(list("abcabc"))  # ['a', 'b', 'c', 'a', 'b', 'c']

# Operations on strings: the count() method
""" The count() method counts all occurrences of the element inside the sequence. The absence of such elements doesn't 
cause any problems. """

print("abcabc".count("b"))  # 2


