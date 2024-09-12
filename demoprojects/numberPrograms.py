################################################################
#### Number programs List

# Armstrong number program
# How to check whether given number is prime or not?
# How to find initial 10 or 20 or 30 …… n prime numbers?
# How to find out 20 (or 30 or 40 …… n) prime numbers after 100 ( or after any given number)?
# How to find out all prime numbers between two given numbers?
# How to find the sum of initial ‘n‘ prime numbers?
# How to find sum of all prime numbers between two given numbers?
# How to print prime numbers between two given numbers in the reverse order?
# How to find the twin prime numbers?
# How to print twin prime numbers between two given numbers?
# How to find a prime number which comes after three non-prime numbers?
# check a palindrome number
# Check number belongs to Fibonacci series or not
# How to find sum of all digits of a number
# check whether user input is number or not
# Roman equivalent of a decimal number
# Generate random numbers

# find largest number less than a given number and without a given digit?
# Reverse and add until you get a palindrome

# Harshad Number (Niven Number) Program
# Magic number program
# How to create a pyramid of numbers


################################################################
# How to check whether given number is prime or not?

from math import sqrt
def checkPrimeNumber(n):
    prime_flag = 0

    if(n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            print("True")
        else:
            print("False")
    else:
        print("False")

# checkPrimeNumber(5)

################################################################
# Armstrong number program

def checkArmstrongNumber(n):

    inputNo = n
    b = len(str(n))
    sum1 = 0
    while n != 0:
        r = n % 10
        sum1 = sum1+(r**b)
        n = n//10
    if inputNo == sum1:
        print("The given number", inputNo, "is armstrong number")
    else:
        print("The given number", inputNo, "is not armstrong number")

# checkArmstrongNumber(15)

################################################################
# check a palindrome string

def isPalindromeUsingSlice(s):
    return s == s[::-1]

def isPalindrome(str):

    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
# print(isPalindrome("teet"))
# print(isPalindromeUsingSlice("teet1"))

################################################################
# check a palindrome number

def checkpalindromeNumber(n):

    input = n
    b = len(str(n))
    sum = 0
    while(n != 0):
        r = n%10
        sum = sum + r*(10**(b - 1))
        b = b - 1
        n = n//10

    if(input == sum):
        print("the no is a palindrome")
        return True
    else:
        print("the no is NOT a palindrome")
        return False

# print(checkpalindromeNumber(12321))   

## One liner solution
""" n = 12321
palindromeFlag = (str(n) == str(n)[::-1])
print(palindromeFlag) """

################################################################


################################################################



################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################


