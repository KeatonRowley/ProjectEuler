a = 1
b = 2


sum = 2 #Include the first of the 2 terms.

while b < 4000000:
    next = a + b  #calculate and swap terms.
    a = b
    b = next
    
    if next % 2 == 0: #add all even integers.
        sum += next
    
    
    
print (sum)



