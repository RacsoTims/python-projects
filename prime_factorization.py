"""
Author: O. Smit

Description:

Prime factorization means determining what the unique prime factors
of an integer are. (For example: 6 can be written as 2 * 3,
the latter numbers being prime). Prime factorization on larger numbers
involves more terms and taking primes to the power of primes.
"""

from sys import argv
from textwrap import dedent
from prime_numbers import PrimeNumberGenerator


def generate_primes(upper_bound):
    primes = PrimeNumberGenerator(3, upper_bound, 2)
    list_of_primes = primes.prime_number_generator()
    return list_of_primes


def division(number, divisor, count):
    remainder = number
    if number % divisor == 0:
        count += 1
        number = number / divisor
        return division(number, divisor, count)
    else:
        return count, remainder


def single_number():
    number = int(input("> "))
    return number


def multiple_numbers():
    lower_bound = int(input("Lower bound: "))
    upper_bound = int(input("Upper bound: "))
    return lower_bound, upper_bound


def main(lower_bound, upper_bound):
    dictionary = {}
    for x in range(lower_bound, upper_bound):
        count = 0

        if x == 1:
            dictionary[x] = 'empty product'
        elif x in list_of_primes:
            dictionary[x] = [f"{x}^1"]
        else:
            list_of_factors = []
            product = 1
            for prime in list_of_primes:
                count, remainder = division(x, prime, count)
                if count > 0:
                    list_of_factors.append(f"{prime}^{count}")
                    product *= prime**count
                count = 0
                x = remainder

                if x in list_of_primes:
                    list_of_factors.append(f"{int(x)}^1")
                    product *= int(x)
                    dictionary[product] = list_of_factors
                    list_of_factors = []
                    break
    return dictionary


list_of_primes = generate_primes(int(argv[1]))

print(dedent("""
            Do you want the prime factors of a particular number
            or of multiple numbers?
                """))
choice = input("\t> ")
if choice == "one":
    number = single_number()
    result = main(number, number + 1)
elif choice == "many":
    lower_bound, upper_bound = multiple_numbers()
    result = main(lower_bound, upper_bound)
else:
    raise Exception("Input unclear. Type either 'one' or 'many'")

for number in result:
    if number == 1:
        print(f"{number}=\t{result[number]}")
    else:
        print(f"{number}=\t", end='')
        for factor in result[number]:
            if len(result[number]) == 1:
                print(factor)
            elif len(result[number]) > 1:
                if factor not in result[number][-1]:
                    print(factor, end=' * ')
                else:
                    print(factor)
