# Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.

def findMaxConsecutiveOnes(nums: list[int]) -> int:
        counter = 0
        maximum = 0
        for i in range(len(nums)):
            if(nums[i] == 1):
                counter += 1
            else:
                counter = 0
            if(counter > maximum):
                maximum = counter
        return maximum

nums = [1, 1, 0, 1, 1, 1]
max = findMaxConsecutiveOnes(nums)
print(f'Array is: {nums}\nMax consecutive ones are: {max}')   