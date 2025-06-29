#  1. Problem Statement: Given an integer N, return the number of digits in N.

n = int(input('Enter a number: '))

def count_digits(n):
    import math
    
    total = int(math.log10(n)) + 1
    return total

# digits = count_digits(n)
# print(f'Total no. of digits in {n} are: {digits}')

# 2. Problem Statement: Given an integer N return the reverse of the given number.

def reverse_number(n):
    num = n
    rev = 0
    while n > 0 :
        temp = n % 10
        rev = (rev * 10) + temp
        n = n // 10
    print(f'Reverse number of {num} is {rev}')

# reverse_number(n)

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
    
# check_palindrome(n)


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

# a = int(input('Enter first number: '))
# b = int(input('Enter second number: '))
# gcd = find_gcd(a, b)
# print(f'GCD of {a} and {b} is: {gcd}')

#  5. Problem Statement: Given an integer N, return true it is an Armstrong number otherwise return false.

def armstrong_number(n):
    k = len(str(n))
    sum = 0
    num = n
    while n > 0:
        temp = n % 10
        sum += temp ** k
        n = n // 10
    if(sum == num):
        print(f'{num} is an armstrong number')
    else:
        print(f'{num} is not an armstrong number')

# armstrong_number(n)

#  6. Problem Statement: Given an integer N, return true it is an Prime number otherwise return false.

def check_prime(n):
    import math
    sqrt = int(math.sqrt(n))
    counter = 0
    for i in range(1, sqrt + 1):
        if(n % i == 0):
            counter += 1
        if(i != n // i):
            counter += 1
    if(counter == 2):
        print(f'{n} is prime number')
    else:
        print(f'{n} is not a prime number')

# check_prime(n)

#  7. Problem Statement: Given an integer N, return all divisors of N.

def find_divisors(n):
    import math
    divisors = list()
    for i in range(1, int(math.sqrt(n)) + 1):
        if(n % i == 0):
            divisors.append(i)
        if(i != n // i):
            divisors.append(n // i)
    print(f'Divisors of {n} are: {sorted(divisors)}')
    
find_divisors(n)