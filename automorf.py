"""
Author: O. Smit

Description:

Determines whether a number is automorphic, i.e.,
whether the last digit of its square
is identical to its own last digit.
"""


def check_if_automorphic(l_bound, u_bound, s_size):
    """Returns a list of automorphic numbers after each number within
    the specified range has been checked for that property.

    :param l_bound:  lower bound
    :type l_bound: int
    :param u_bound: upper bound
    :type u_bound: int
    :param s_size: step size
    :type s_size: int

    :rtype: list
    :return: list of automorphic numbers
    """
    automorphic = []
    for test in range(l_bound, u_bound, s_size):
        if str(test)[-1] == str(test**2)[-1]:
            automorphic.append(test)
    return automorphic


l_bound = int(input("Lower bound: "))
u_bound = int(input("Upper bound: "))
s_size = int(input("Step size: "))

my_list = check_if_automorphic(l_bound, u_bound, s_size)
print(f"Deze getallen zijn automorfe getallen:")
for number in my_list:
    print(number)
