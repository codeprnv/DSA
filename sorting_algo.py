import random

# Selection Sort

# Step 1: Find the minimum in the array. (Consider the starting element as minimum at the beginning => initial pointer )
# Step 2: Replace the current minimum(starting element) with the actual minimum found in the array
# Step 3: Repeat the step 2 while updating the current minimum element

def selection_sort(arr: list[int]):
    for i in range(0, len(arr) - 1):
        mini = i
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[mini] ):
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
    return arr

arr = [random.randint(1, 120) for _ in range(7)]
print(f'The unsorted array is: {arr}\nThe sorted array using selection sort is: {selection_sort(arr)}')

# Bubble Sort

# Step 1: Compare the adjacent elements in the array and push the maximum element to end for each iteration
# Step 2: Repeat this step until the array is sorted. Consider the current element as maximum initially the first

def bubble_sort(arr: list[int]):
    for i in range(len(arr) - 1):
        didSwap = 0
        for j in range(len(arr) - 1 - i):
            if(arr[j] > arr[j + 1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                didSwap = 1
        if(didSwap == 0):
            break
    return arr

arr = [random.randint(1, 120) for _ in range(7)]
print(f'The unsorted array is: {arr}\nThe sorted array using bubble sort is: {bubble_sort(arr)}')

# Insertion Sort

#  Step 1: Initialize the first element as sorted
#  Step 2: Pick the next element in the array and insert it into the sorted array
#  Step 3: Repeat step 2 until the entire array is sorted

def insertion_sort(arr: list[int]):
    for i in range(len(arr)):
        j = i
        while(j > 0 and arr[j - 1] > arr[j]):
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j-=1
    return arr

arr = [random.randint(1, 120) for _ in range(7)]
print(f'The unsorted array is: {arr}\nThe sorted array using insertion sort is: {insertion_sort(arr)}')