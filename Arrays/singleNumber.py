#  Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

def singleNumber(nums: list[int]) -> int:
    XOR = 0
    for i in range(len(nums)):
        XOR = XOR ^ nums[i]
    return XOR

nums = [4,1,2,1,2]
res = singleNumber(nums)
print(f'Array is: {nums}\nSingle number is: {res}')