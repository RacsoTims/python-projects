"""
Author: O. Smit

Description:

Generates a list of prime numbers to be exported and used in other files.
"""


class PrimeNumberGenerator(object):

    def __init__(self, lower_bound, upper_bound, step_size):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.step_size = step_size

    def prime_number_generator(self):
        prime_number = []
        prime_number.append(2)
        for x in range(self.lower_bound, self.upper_bound, self.step_size):
            divisors = []
            for y in range(3, x):
                if (x % y == 0):
                    divisors.append(y)
                    break
            if(len(divisors) == 0 and x != 1):
                prime_number.append(x)
        return prime_number
