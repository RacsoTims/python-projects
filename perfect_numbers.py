"""
Author: O. Smit

Description:

Determines whether a number is a perfect number, i.e.,
if its proper divisors add to itself exactly.
"""


def perfect_numbers(lower_bound, upper_bound, step_size):
    hits = {}
    for number in range(lower_bound, upper_bound, step_size):
        divisors = []
        for divisor in range(1, number):
            if(number % divisor == 0):
                divisors.append(divisor)
        if sum(divisors) == number:
            sum_divisors = '+'.join(map(str, divisors))
            hits[number] = sum_divisors
    return hits


l_bound = int(input("Lower bound: "))
u_bound = int(input("Upper bound: "))
s_size = int(input("Step size: "))

result = perfect_numbers(l_bound, u_bound, s_size)

if len(result) != 0:
    print("  Results:")
    for hit in result:
        print(f"{hit}  ({result[hit]})")
else:
    print("There are no numbers in that range that qualify.")
