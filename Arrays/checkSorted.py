import random
def checkSorted(nums):
    for i in range(len(nums) - 1):
        if(nums[i] > nums[i + 1]):
            return False
    return True

nums = [random.randint(1, 100) for _ in range(7)]
result = checkSorted(nums)
if(result):
    print(f'Array is sorted: {nums}')
else:
    print(f'Array is not sorted: {nums}')