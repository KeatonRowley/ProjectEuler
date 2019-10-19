#determins if a number is a palindrome
def is_palindrome(num):
    numStr = str(num)
    numStrLen = len(numStr)
    for index in range(numStrLen):
        if(numStr[index] != numStr[numStrLen - index -1] ):
            return False
    return True

#calculates largest palindrome of product of 3 digit numbers
def largest_palindrome_three_digit():
    largest_palindrome = 0
    for i in range(999):
        for j in range(999):
            product = i*j
            if(is_palindrome(product) and product > largest_palindrome):
                largest_palindrome = product
    return largest_palindrome

print(largest_palindrome_three_digit())

