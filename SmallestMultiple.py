#   Solution to Project Euler problem 5
#   Copyright (c) Project Keaton Rowley. All rights reserved.
#   https://github.com/KeatonRowley/ProjectEuler

#Calculates the smallest multiple of the first num numbers
# multiplied
def smallest_multiple(num):
    total = 1
    for i in range(num):
        total *= i
    
    for i in range(2,num):
        for j in range(2,num):
          /  product = i*j
            if total % product == 0:
                total /= product
    return total

print(smallest_multiple(20))