def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


pw = [x for x in powers_of_2(5)]  # List Comprehension
print(pw)

pw = list(powers_of_2(3))  # list() function
print(pw)

# ---------------------------------------------------------------------------------------------------------------------

the_list = []

for x in range(10):
    # expression_one if condition else expression_two
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list)

# ---------------------------------------------------------------------------------------------------------------------


# It's the parentheses. The brackets make a comprehension, the parentheses make a generator.
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()

# ---------------------------------------------------------------------------------------------------------------------

