def char_count():
    n = int(input('Enter the size of array: '))
    arr = list()
    for i in range(n):
        arr.append(int(input(f'Enter the element at {i} position: ')))

    hash_dict = {}
    for num in arr:
        hash_dict[num] = hash_dict.get(num, 0) + 1
    print(f'Array is: {arr}')
    print(f'Hash Array is: {hash_dict}')
char_count()

def calculate_lucky_number(s: str, n: int):
    sum = 0
    for i in range(1, n + 1):
        ascii = ord(s[i - 1])
        if(i % 2 != 0 or ascii % 2 != 0):
            sum += ascii * i
    return sum

s = str(input('Enter your name: '))
result = calculate_lucky_number(s, len(s))
print(f'Your lucky number is: {result}')

def element_frequency():
    n = int(input('Enter the size of array: '))
    arr = [int(input(f'Enter the element at {i} position: ')) for i in range(n)]
    print(f'Array is: {arr}')
    hash_dict = {}
    for num in arr:
        hash_dict[num] = hash_dict.get(num, 0) + 1
    print(f'Hash Map is: {hash_dict}')
    min_num, max_num = None, None
    min_val, max_val = min(hash_dict.values()), max(hash_dict.values())
    for num, value in hash_dict.items():
        if value == min_val and min_num is None:
            min_num = num
        if value == max_val and max_num is None:
            max_num = num
        if min_num is not None and max_num is not None:
            break
    return min_num, max_num

min_num, max_num = element_frequency()
print(f'Element with minimum frequency is: {min_num}\nElement with maximum frequency is: {max_num}') 


# Changes