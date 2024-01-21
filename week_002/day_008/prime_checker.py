# Write your code below this line 👇

import math


def prime_checker(num):
    if num <= 1:
        return "It's not a prime number."
    if num <= 3:
        return "It's a prime number."
    if num % 2 == 0 or num % 3 == 0:
        return "It's not a prime number."
    sqrt_n = int(math.sqrt(num)) + 1
    for i in range(5, sqrt_n, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return "It's not a prime number."
    return "It's a prime number."


n = int(input("Enter an integer: "))

print(prime_checker(n))
