#calculates the largest specialPythagorianTriplet
#which equals num

def specialPythagorainTriplet(num):
    nums = -1
    
    for a in range(1,num):
        for b in range(1,num):
            if ((a**2+b**2)**.5 + a + b)== num: #if sqrt(a^2+b^2)
                return a * b * (a**2+b**2)**.5

    return int(nums)

print(specialPythagorainTriplet(300))