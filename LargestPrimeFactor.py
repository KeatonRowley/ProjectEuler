def isPrime(number):
    for val in range(2, number):
        if(number % val == 0):
            return False
    return True

def getFactors(number):
    factors = []
    max = 2
    #Add factors to an array.
    for val in range(2, number):
        if(number % val == 0):
            max = number / val
            if val > max: # stop when all factors found.
                break
            factors.append(val)
            factors.append(int(number / val))
    #get factors in correct order
    factors.sort() 
    return factors

#Gets largest prime factor of an input number
def largest_prime_factor(input):
    factors = getFactors(input)
    for val in reversed(factors):
        if(isPrime(val)):
            return val
    return -1 #return -1 if value not found. 
   

   
print(largest_prime_factor(600851475143))