import random
#  Left rotate a given array nums by k-places

def leftRotate(nums):
    k = int(input(f'Array is: {nums}\nEnter the places to left rotate the array: '))
    if(k > len(nums)):
        k = k % len(nums)
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    nums[:] = reversed(nums)

nums = [random.randint(1, 100)for _ in range(6)]
leftRotate(nums)
print(f'After rotation: {nums}')


# Right rotate the given array nums by k-places

def rightRotate(nums):
    k = int(input(f'Array is: {nums}\nEnter the places to right rotate the array: '))
    if(k > len(nums)):
        k = k % len(nums)
    nums[:] = reversed(nums)
    nums[k:] = reversed(nums[k:])
    nums[:k] = reversed(nums[:k])

nums = [random.randint(1, 100)for _ in range(6)]   
rightRotate(nums)
print(f'After rotation: {nums}')