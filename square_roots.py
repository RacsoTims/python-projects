"""
Author: O. Smit

Description:

Approximates the square root of a number without using the 'sqrt()' function.
"""


from sys import argv
from numpy import sqrt


def compute_digit(number, digits, nth_digit):
    for i in range(1, 11):
        j = (i + digits)**2

        if number - j < 0:

            if len(list_of_digits) < 4:
                list_of_digits.append(str(i - 1))
                list_of_digits_strung = int(''.join(list_of_digits[0:4]))
                digits = list_of_digits_strung * 10
                nth_digit += 1
                return compute_digit(number*100, digits, nth_digit)
            else:
                return digits, nth_digit
        elif number - j == 0:
            list_of_digits.append(i)
            digits = list_of_digits[0]
            return digits, nth_digit


list_of_digits = []
digits = 0
nth_digit = 0

for number in range(int(argv[1]), int(argv[2])):
    nth_digit_sum, nth_digit_amount = \
        compute_digit(number, digits, nth_digit)
    approximation = nth_digit_sum / 10**(nth_digit_amount)
    print(f"{number}≈", end='\t')
    print(f"{approximation}", end='\t')
    print(f"{round(sqrt(number) - approximation, 4)}")
    list_of_digits = []
