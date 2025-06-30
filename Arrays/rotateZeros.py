# Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the end of the array and 
# move non-negative integers to the front by maintaining their order.

def rotateZeros(nums):
    j = -1 #Tracks the first zero element
    for i in range(len(nums)):
        if(nums[i] == 0):
            j = i #Initializes j with the index of first zero and breaks the loop
            break
    if(j == -1): #Executes if no zero is found after the iteration. Stops further execution of program
        return
    for i in range(j + 1, len(nums)): #Starts new iteration 1 position ahead of first zero till the length of the array
        if(nums[i] != 0): #Checks if the elements are non-zeros and swaps those with the first zero for each iteration
            nums[j], nums[i] = nums[i], nums[j]
            j += 1 #Increments the j position by 1

nums = [1,2,0,1,0,4,0]
print(f'Array is: {nums}')
rotateZeros(nums)
print(f'After rotating all the zeros to the end: {nums}')