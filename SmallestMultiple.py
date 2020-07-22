#   Solution to Project Euler problem 5
#   Copyright (c) Project Keaton Rowley. All rights reserved.
#   https://github.com/KeatonRowley/ProjectEuler


# Get the next prime given a list of primes in order.
def next_prime(prime_list):
    start = prime_list[-1]
    next_found = False
    while next_found == False:
        start += 1
        is_prime = True
        for num in prime_list:
            if start % num == 0:
                is_prime = False
                break
        next_found = is_prime
    return start
                
    

# Get dict of all prime factors of a number
# key = factor, val = power
def prime_factors(number):
    curr = number
    prime_factors = {}
    prime_num_list = [2]
    curr_prime = 2
    while curr != 1:
        # If it is a factor, store it. Else move to the next prime.
        if curr % curr_prime == 0:
            curr /= curr_prime
            if curr_prime in prime_factors:
                prime_factors[curr_prime]+=1
            else:
                prime_factors[curr_prime]=1
        else:
            curr_prime = next_prime(prime_num_list)
            prime_num_list.append(curr_prime)

    return prime_factors




# Calculates the smallest multiple of the first num numbers
# multiplied
def smallest_multiple(num):
    lcm_dict = {}

    for i in range(1,num+1):
        temp = prime_factors(i)
      
        for key in temp:   # union the two dictionaries keeping factors with greater power.
            if key in lcm_dict:
                lcm_dict[key] = lcm_dict[key] if lcm_dict[key] > temp[key] else temp[key]
            else:
                lcm_dict[key] = temp[key]
    lcm = 1
    for factor in lcm_dict:
        lcm *= factor**lcm_dict[factor]
    return lcm

print(smallest_multiple(20))