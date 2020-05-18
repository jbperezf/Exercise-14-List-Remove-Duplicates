# Exercise 14. List Remove Duplicates
#
# Write a program (function!) that takes a list and returns a new list that contains all the elements of the
# first list minus all the duplicates.
#
# Extras:
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

import random


def remove_list_duplicates(x):
    return list(set(x))


# Exercise 5. Revisited


def exc_5_func(list_a, list_b):
    list_c = []
    for i in list_a:
        if i in list_b and i not in list_c:
            list_c.append(i)
    return list_c


a = [random.randrange(1, 13, 1) for i in range(11)]
b = [random.randrange(1, 13, 1) for i in range(13)]
c = []

print(exc_5_func(a, b))
print(remove_list_duplicates(i for i in a if i in b and i not in c))
