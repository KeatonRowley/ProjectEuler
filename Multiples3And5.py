sum = 0

for val in range(3, 1000):
    if val % 3 ==0 or val % 5 == 0:
        sum += val

print(sum)