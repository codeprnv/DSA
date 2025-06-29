#  Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.

def secondLargest(nums):
    l1 = nums[0]
    l2 = -1
    for i in range(1, len(nums)):
        if(nums[i] > l1):
            l2 = l1
            l1 = nums[i]
        elif(nums[i] < l1 and nums[i] > l2):
            l2 = nums[i]
    return l2

nums = [3, 56, 0, 99, -40]
sLargest = secondLargest(nums)
print(f'Array is: {nums}')
print(f'The second largest element in this array is: {sLargest}')