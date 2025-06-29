import random

# Linear Search

def linear_search(arr: list[int], target: int):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [random.randint(0, 100) for _ in range(8)]
print(arr)
target = int(input('Enter the number to search: '))
res = linear_search(arr, target)
if(res == -1):
    print(f'{target} not found in the list')
else:
    print(f'{target} found at {res} index')    

 
#  Binary Search

#  Step 1: Binary Search function takes the list of elements to search from, the lower limit which is initially set to 0 and the higher limit which is the
#          length of the list - 1 and the target number to search
#  Step 2: Check the length of list is greater than 1 and while the lower limit is less than or equal to the higher limit recursively find the midpoint and compare the mid element with the target number
#  Step 3: Find the midpoint = low + (high - low) // 2
#  Step 4: Compare the mid element with the target value, if equal return the index of mid element else check whether the mid element is less or greater than the target element then based upon it find the left sub-array or right sub-array recursively
#  Step 5: If the mid element is greater than the target value call the binary_search() on left sub-array with the low limit as it is and the higher limit upto mid - 1
# vice-versa if the mid element is lesser than target value (low = mid + 1, high) 


def binary_search(arr: list[int], low: int, high: int , target: int):
    if len(arr) == 1:
        return 0
    while(low <= high):
        mid = low + (high - low) // 2
        if(arr[mid] == target):
            return mid
        elif(arr[mid] > target):
            return binary_search(arr, low, mid - 1, target)
        else:
            return binary_search(arr, mid + 1 , high, target)
    return -1
        
arr = [random.randint(0, 100) for _ in range(8)]
arr.sort()
print(f'The list to search is: {arr}')
target = int(input('Enter the number to search: '))
res = binary_search(arr, 0, len(arr) - 1, target)
if(res == -1):
    print(f'{target} was not found in the list')
else:
    print(f'{target} found at {res} index')