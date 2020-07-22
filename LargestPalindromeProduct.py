#   Solution to Project Euler problem 4
#   Copyright (c) Project Keaton Rowley. All rights reserved.
#   https://github.com/KeatonRowley/ProjectEuler

# determines if a number is a palindrome
def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

# calculates largest palindrome of product of 3 digit numbers
def largest_palindrome_three_digit():
    largest_palindrome = 0
    for i in range(999):
        for j in range(999):
            product = i*j
            if(is_palindrome(product) and product > largest_palindrome):
                largest_palindrome = product
    return largest_palindrome

print(largest_palindrome_three_digit())

