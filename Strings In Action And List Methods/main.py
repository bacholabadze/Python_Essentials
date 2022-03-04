""" Python is not aware (it cannot be in any way) of subtle linguistic issues -
it just compares code point values, character by character."""

# 'alpha' == 'alpha'  True
# 'alpha' != 'Alpha'  True

""" The final relation between strings is determined by comparing the first different character in both strings
(keep ASCII/UNICODE code points in mind at all times.)"""


""" When you compare two strings of different lengths and the shorter one is identical to the longer one's beginning,
the longer string is considered greater"""

# 'alpha' < 'alphabet' True


""" String comparison is always case-sensitive (upper-case letters are taken as lesser than lower-case). """

# 'beta' > 'Beta' True


""" Even if a string contains digits only, it's still not a number. It's interpreted as-is, like any other regular 
string, and its (potential) numerical aspect is not taken into consideration in any way."""

# '10' == '010'  False
# '10' > '010'   True
# '10' > '8'     False
# '20' < '8'     True
# '20' < '80'    True


# Comparing strings against numbers is generally a bad idea.
""" The only comparisons you can perform with impunity are these symbolized by the == and != operators.
The former always gives False, while the latter always produces True"""

# '10' == 10  False
# '10' != 10  True
# '10' == 1   False
# '10' != 1   True
# '10' > 10   TypeError exception


# The sorted() function:
""" The function takes one argument (a list) and returns a new list, filled with the sorted argument's elements.
[!] The original list remains untouched. """

first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)  # ['omega', 'alpha', 'pi', 'gamma']
print(first_greek_2)  # ['alpha', 'gamma', 'omega', 'pi']


# The sort() method:
""" The second method affects the list itself - [!] no new list is created.
Ordering is performed in situ by the method named sort()."""

second_greek = ['omega', 'alpha', 'pi', 'gamma']
second_greek.sort()

print(second_greek)  # ['alpha', 'gamma', 'omega', 'pi']
