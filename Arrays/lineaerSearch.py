# Problem Statement: Given an array, and an element num the task is to find if num is present in the given array or not. 
# If present print the index of the element or print -1.

def linearSearch(nums, target):
    found = -1
    for i in range(len(nums)):
        if(nums[i] == target):
            return i
    return found

import random
nums = [random.randint(1, 100)for _ in range(7)]
print(f'Array is: {nums}')
target = int(input('Enter the number to find: '))
result = linearSearch(nums, target)
if(result == -1):
    print(f'{target} not found in the array')
else:
    print(f'{target} found at {result} index')