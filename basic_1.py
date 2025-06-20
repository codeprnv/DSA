#  1. Problem Statement: Given an integer N, return the number of digits in N.

n = int(input('Enter a number: '))

def count_digits(n):
    import math
    
    total = int(math.log10(n)) + 1
    print(f'Total no. of digits in {n} are: {total}')

count_digits(n)

# 2. Problem Statement: Given an integer N return the reverse of the given number.

def reverse_number(n):
    num = n
    rev = 0
    while n > 0 :
        temp = n % 10
        rev = (rev * 10) + temp
        n = n // 10
    print(f'Reverse number of {num} is {rev}')

reverse_number(n)

#  3. Problem Statement: Given an integer N, return true if it is a palindrome else return false.

def check_palindrome(n):
    num = n
    rev = 0
    while n > 0:
        temp = n % 10
        rev = (rev * 10) + temp
        n = n // 10
    if(rev == num):
        print(f'The number {num} is palindrome')
    else:
        print(f'The number {num} is not palindrome')
    
check_palindrome(n)


#  4. Problem Statement: Given two integers N1 and N2, find their greatest common divisor.
def find_gcd(a: int, b: int):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    if(a == 0):
        return b 
    return a

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
gcd = find_gcd(a, b)
print(f'GCD of {a} and {b} is: {gcd}')