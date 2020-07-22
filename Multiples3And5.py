#   Solution to Project Euler problem 1
#   Copyright (c) Project Keaton Rowley. All rights reserved.
#   https://github.com/KeatonRowley/ProjectEuler

# Calculates the sum of all multiples 3 & 5 for 1st
# thousand numbers.

# Use k + 2k + 3k+ 4k... = kn(n+1)/2 summation identity.
def arithmetic_sum(k, n):
    return int(k*n*(n + 1) / 2)

def get_sum_multiples_three_five(range):
    range_three = int(range / 3)
    range_five = int(range / 5 - 1)
    
    # calculate the join to be removed from combination
    range_fifteen = int(range / 15)

    # get 3 summations
    three_sum = arithmetic_sum(3, range_three)
    five_sum = arithmetic_sum(5, range_five)
    fifteen_sum = arithmetic_sum(15, range_fifteen)

    return three_sum + five_sum - fifteen_sum

print(get_sum_multiples_three_five(1000))