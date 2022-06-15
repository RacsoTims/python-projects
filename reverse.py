"""
Author: O. Smit

Description:

Checks whether there are numbers that when multiplied by
a number between two and ten, the resulting number is the
original number if read from right to left.
"""


def reverse_digits(l_bound, u_bound, s_size):
    hits = []
    for number in range(l_bound, u_bound, s_size):
        for factor in range(2, 10):
            number_backwards = str((number * factor))[::-1]
            if number_backwards == str(number):
                hits.append(f"{number} {number * factor} {factor}x")
    return hits


l_bound = int(input("Lower bound: "))
u_bound = int(input("Upper bound: "))
s_size = int(input("Step size: "))

result = reverse_digits(l_bound, u_bound, s_size)

if len(result) != 0:
    print("  Results:")
    for hit in result:
        print(hit)
else:
    print("There are no numbers in that range that qualify.")
