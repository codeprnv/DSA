# Given an integer array nums sorted in non-decreasing order, remove all duplicates in-place so that each unique element appears only once. Return the number of unique elements in the array.

# If the number of unique elements be k, then,

# Change the array nums such that the first k elements of nums contain the unique values in the order that they were present originally.
# The remaining elements, as well as the size of the array does not matter in terms of correctness.

# An array sorted in non-decreasing order is an array where every element to the right of an element is either equal to or greater in value than that element.

def uniqueElements(nums):
    i = 0
    for j in range(1, len(nums) - 1):
        if(nums[j] != nums[i]):
            nums[i + 1] = nums[j]
            i += 1
    return i + 1

nums = [-2, 2, 4, 4, 4, 4, 5, 5]
result = uniqueElements(nums)
print(f'Array is: {nums}\nLength of the array without duplicates is: {result}')