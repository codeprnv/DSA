# s = str(input('Enter a string: '))
# result = ''
# for i in range(len(s) - 1, -1, -1):
#     result += s[i]
# print(f'The string is: {s}\nReversed String is: {result}')

# Check Prime

# num = int(input('Enter a number: '))
# if num < 2:
#     print(f'{num} is not a prime number')
# else:
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if(num % i == 0):
#             is_prime = False
#             break
#     if is_prime:
#         print(f'{num} is a prime number')
#     else:
#         print(f'{num} is not a prime number')


num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

print(f'Num1: {num1}\nNum2: {num2}')

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f'Num1: {num1}\nNum2: {num2}')