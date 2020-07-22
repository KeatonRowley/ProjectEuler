#   Solution to Project Euler problem 9
#   Copyright (c) Project Keaton Rowley. All rights reserved.
#   https://github.com/KeatonRowley/ProjectEuler

#calculates the largest specialPythagorianTriplet
#which equals num

def special_pythagorean_triplet(num):
    nums = -1
    
    for a in range(1,num):
        for b in range(1,num):
            if ((a**2+b**2)**.5 + a + b)== num: #if sqrt(a^2+b^2)
                return a * b * (a**2+b**2)**.5

    return int(nums)

print(special_pythagorean_triplet(1000))