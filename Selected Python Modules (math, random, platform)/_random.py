""" The most general function named random() (not to be confused with the module's name) produces a float number x
coming from the range (0.0, 1.0) - in other words: (0.0 <= x < 1.0). """

from random import random, seed, randint, randrange, choice, sample

""" The seed() function is able to directly set the generator's seed. We'll show you two of its variants:

seed() - sets the seed with the current time;
seed(int_value) - sets the seed with the integer value int_value. """

seed()  # "freezes random"

for i in range(5):
    print(random())
    # 0.20985124453651727
    # 0.3853979112650403
    # 0.19506031439111238
    # 0.3956006670655835
    # 0.5626807809272817 (always same if seed() has arg)

"""
randrange(end)
randrange(beg, end)
randrange(beg, end, step)
randint(left, right)

range(end)
range(beg, end)
range(beg, end, step)

choice(sequence)
sample(sequence, elements_to_choose)
"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))  # 4
print(sample(my_list, 5))  # [10, 3, 5 8, 2]
