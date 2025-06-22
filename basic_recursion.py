# 1. Problem: Print your Name N times using recursion
def print_name(i, count, name):
    if(i > count):
        return
    print(f'{i} : {name}')
    print_name(i + 1, count, name)

name = str(input('Enter your name: '))
count = int(input('No. of times the name to be printed: '))
print_name(1, count, name)

# 2. Problem: Print from 1 to N using Recursion

def print_numbers(i, num):
    if(i > num):
        return 
    print(i)
    print_numbers(i + 1, num)

num = int(input('Enter the numbers to print: '))
print_numbers(1, num)

# 3. Problem: Print from N to 1 using Recursion

def print_reverseNumbers(i, num):
    if(i < num):
        return
    print(i)
    print_reverseNumbers(i - 1, num)
    
num = int(input('Enter the numbers to print: '))
print_reverseNumbers(num, 1)

# 4. Problem statement: Given a number ‘N’, find out the sum of the first N natural numbers.

def sum_of_numbers(n):
    sum = n * (n + 1) // 2
    print(f'Sum of first {n} numbers is: {sum}')

n = int(input('Enter the number: '))
sum_of_numbers(n)

# 5. Problem Statement: Given a number X,  print its factorial.
def factorial(n):
    if(n == 0):
        return 1
    return n * factorial(n - 1)

n = int(input('Enter the number: '))
print(f'Factorial of {n} is: {factorial(n)}')

# 6. Problem Statement: You are given an array. The task is to reverse the array and print it. 
def reverse_array(n):
    arr = list()
    for i in range(1, n + 1):
        val = int(input(f'Enter the element at {i} position: '))
        arr.append(val)
    print(f'Array is: {arr}')
    print(f'Reversed array is: {arr[::-1]}')

n = int(input('Enter the size of array: '))
reverse_array(n)


# 7. Problem Statement: "Given a string, check if the string is palindrome or not."  A string is said to be palindrome if the reverse of the string is the same as the string.
def check_palindrome(s):
   left = 0
   right = len(s) - 1
   while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
        return True

string = str(input('Enter the string: '))
res = check_palindrome(string)
if(res):
    print(f'{string} is a palindrome string')
else:
    print(f'{string} is not a palindrome string')

def fibonacci(n):
    a = 0
    b = 1
    print(a, end=' ')
    for i in range(n):
        a, b = b, a + b
        print(a, end=' ')
        
n = int(input('Enter the number: '))
print(f'Fibonacci Series for {n} is: ',end=' ')
fibonacci(n)