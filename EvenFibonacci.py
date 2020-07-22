#   Solution to Project Euler problem 2
#   Copyright (c) Project Keaton Rowley. All rights reserved.
#   https://github.com/KeatonRowley/ProjectEuler

# Get the sum of all the Fibonacci sequence whose values don't exceed 4
# million.
def get_first_sum_even_num(limit):
    a = 1
    b = 2
    sum = 2 # Include the first of the 2 terms.

    while b < limit:
        next = a + b  # calculate and swap terms.
        a = b
        b = next
        
        if next % 2 == 0: # add all even integers.
            sum += next
    
    return sum
        
    
    
print(get_first_sum_even_num(4000000))



