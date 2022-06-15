"""
Author: O. Smit

Description:

Generates and prints a list of twin primes based on
the input list of prime numbers.
"""


from prime_numbers import PrimeNumberGenerator
from sys import argv


def generate_primes():
    primes = PrimeNumberGenerator(3, int(argv[1]), 2)
    list_of_primes = primes.prime_number_generator()
    return list_of_primes


def generate_twin_primes(list_of_primes):
    twin_primes = []
    for i in list_of_primes:
        if i + 2 in list_of_primes:
            twin_primes.append(i)
            twin_primes.append(i + 2)
        else:
            continue
    return twin_primes


def print_twin_primes(twin_primes):
    print(f"Number of twins: {len(twin_primes) / 2}:")
    for j in range(0, len(twin_primes) - 1, 1):
        if twin_primes[(j + 1)] - twin_primes[j] == 2:
            pair = twin_primes[j: (j + 2): 1]
            print(pair)
        else:
            continue


print("The following are twin prime numbers:")
my_primes = generate_primes()
my_twin_primes = generate_twin_primes(my_primes)
my_twin_primes_printed = print_twin_primes(my_twin_primes)
