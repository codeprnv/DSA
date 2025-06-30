# Problem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. 
# Find the number(between 1 to N), that is not present in the given array.

def missingNumber(nums):
    n = len(nums)
    sum = n  * (n + 1) // 2
    sum2 = 0
    for i in range(len(nums)):
        sum2 += nums[i]
    return (sum - sum2)

nums = [0, 1, 2, 4, 5]
print(f'Array is: {nums}')
res = missingNumber(nums)
print(f'Missing number from the array is: {res}')