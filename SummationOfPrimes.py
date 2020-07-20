#   Solution to Project Euler problem 10
#   Copyright (c) Project Keaton Rowley. All rights reserved.
#   https://github.com/KeatonRowley/ProjectEuler

def newPrime(start, num):
    for val in range(start, int(num**0.5)):
        if(num % val == 0):
            return False
    return True

def sumValues(array):
    sum =0
    for item in array:
        sum += item
    return sum

def summationOfPrimes():
    primes = [2]
    for val in range(3,2000000,2):
        isPrime = True
        for prime in primes:
            if val % prime == 0:
                isPrime = False
                break
        #If not already divisible by current primes, check
        #to see if it is a new prime starting at last known prime all the way to 
        #number.
        if isPrime == True and newPrime(primes[len(primes)-1], val):
            primes.append(val) 
    return sum(primes)
print(summationOfPrimes())
