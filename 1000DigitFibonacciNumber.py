#   Solution to Project Euler problem 25
#   Copyright (c) Project Keaton Rowley. All rights reserved.
#   https://github.com/KeatonRowley/ProjectEuler

def digit_count(input):
    return len(str(input)) < 1000

def get_1000th_fibonacci():
    first = 1
    second = 1
    index = 1
    while digit_count(second): 
        next = first + second
        first = second
        second = next
        index += 1
    return index

print(get_1000th_fibonacci())