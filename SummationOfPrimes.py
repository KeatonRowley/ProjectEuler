#   Solution to Project Euler problem 10
#   Copyright (c) Project Keaton Rowley. All rights reserved.
#   https://github.com/KeatonRowley/ProjectEuler


# Given a value n, calculates the sum of all
# prime numbers less than that value and returns it.
def summation_of_primes(n):
    prime_list = [True for x in range(n+1)]

    curr = 2
    while(curr**2 <= n):
        if prime_list[curr]:
            for i in range(curr, n+1, curr):
                prime_list[i] = False
        curr += 1


    total = sum([i for i, val in enumerate(prime_list) if val])
    return total

print(summation_of_primes(2000000))

