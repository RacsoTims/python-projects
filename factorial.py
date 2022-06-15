"""
Author: O. Smit

Description:

Calculates the factorial of any positive integer n,
or the choose function for any positive integers
n and k
"""


def get_factorial(number, result):
    for factor in range(2, number + 1):
        result *= factor
    return result


def choose_function(n, k, result):
    x = get_factorial(n, result)
    y = get_factorial(k, result)
    z = get_factorial((n - k), result)
    w = x / (y * z)
    return w


start = 1

print("Do you want the factorial of n (1)\
 or the choose function for n and k (2)?")
choice = input("> ")
if choice == "1":
    n = int(input("Value of n: "))
    answer = get_factorial(n, start)
    print(f"Your answer: {answer}.")
if choice == "2":
    n = int(input("Value of n: "))
    k = int(input("Value of k: "))
    answer = choose_function(n, k, start)
    print(f"Your answer: {answer}.")
