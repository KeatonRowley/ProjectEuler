#   Solution to Project Euler problem 13
#   Copyright (c) Project Keaton Rowley. All rights reserved.
#   https://github.com/KeatonRowley/ProjectEuler

# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

f = open("LargestSumProblem13InputText.txt")

input = f.read().splitlines() #.strip()
input = list(map(int, input))

sum = sum(input)

sum_to_string = str(sum)

# print(sum)
print(sum_to_string[0:10])
