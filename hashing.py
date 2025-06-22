n = int(input('Enter the size of array: '))
arr = list()
for i in range(n):
    arr.append(int(input(f'Enter the element at {i} position: ')))

hash_dict = {}
for num in arr:
    hash_dict[num] = hash_dict.get(num, 0) + 1
print(f'Array is: {arr}')
print(f'Hash Array is: {hash_dict}')