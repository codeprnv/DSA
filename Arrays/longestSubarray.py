# Calculate longest subarray with the sum k 
def longestSubArray(arr: list[int], k: int) -> int:
    n = len(arr) # Take the size of the array
    # Create empty dictionary (Map)
    preSumMap = {}
    Sum = 0
    maxLen = 0
    for i in range(n):
        # Calculate the sum of elements upto i
        Sum += arr[i]
        # If the sum is equal to k update maxLength to maximum of maxLen and i + 1
        if Sum == k:
            maxLen = max(maxLen, i + 1)
        # Calculate sum of the remaining part i.e (x - k)
        rem = Sum - k
        # Calculate the length and update the maximum
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)
        # Finally update the map checking the conditions
        if Sum not in preSumMap:
            preSumMap[Sum] = i
    return maxLen

arr = [-1, 1, 1]
k = 1
length = longestSubArray(arr, k)
print(f'Array is: {arr}\nMaximum SubArray is of length: {length}')