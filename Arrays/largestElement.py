# Given an array of integers nums, return the value of the largest element in the array

def largest_element(arr):
    print(f'Array is: {arr}')
    largest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest
    
nums = [3, 3, 0, 99, -40]
largest = largest_element(nums)
print(f'The largest element in the array is: {largest}')

# The time complexity for this solution is O(n) which is the optimal solution for this problem
# Another way is through brute force using sorting algorithms like merge sort which has time complexity of O(n log n)

