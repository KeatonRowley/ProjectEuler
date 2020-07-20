# Keaton Rowley 6-29-2020
# Large sum problem 13
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

f = open("LargestSumProblem13InputText.txt")

input = f.read().splitlines() #.strip()
input = list(map(int, input))

sum = sum(input)

sum_to_string = str(sum)

# print(sum)
print(sum_to_string[0:10])
