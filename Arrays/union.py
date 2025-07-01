# Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.
# The union of two arrays can be defined as the common and distinct elements in the two arrays.
# NOTE: Elements in the union should be in ascending order.

def union(arr1, arr2):
    # Know the length of the two arrays first
    n = len(arr1)
    m = len(arr2)
    # Initialize two pointers with 0 i.e first element
    i = 0
    j = 0
    # Initialize a new union array which will store unique elements from both the arrays
    union_arr = []
    # Iterate over both the arrays till the last element in both the arrays
    while(i < n and j < m):
        print(i, '=>', j)
        # Check if the element is smaller in the first array than the second one
        if(arr1[i] <= arr2[j]):
            # Check if the union array is empty for first time and it doesn't contain same element twice
            if(len(union_arr) == 0 or union_arr[len(union_arr) - 1] != arr1[i]):
                union_arr.append(arr1[i]) # Add the unique element from the first array to the union array
            # Increment the i pointer by 1
            i += 1
        else:
            # Repeat same for second array
            if(len(union_arr) == 0 or union_arr[len(union_arr) - 1] != arr2[j]):
                union_arr.append(arr2[j])
            j += 1
    # If the first array gets exhausted loop for the rest of the second array
    while(j < m):
        if(len(union_arr) == 0 or union_arr[len(union_arr) - 1] != arr2[j]):
                union_arr.append(arr2[j])
        j += 1
    # If the second array gets exhausted then loop for the rest of first array
    while(i < n):
        if(len(union_arr) == 0 or union_arr[len(union_arr) - 1] != arr1[i]):
            union_arr.append(arr1[i])
    # Return the union array at last
    return union_arr

arr1 = [1,2,3,4,5,6,7,8,9,10]
arr2 = [2,3,4,4,5,11,12]

res = union(arr1, arr2)
print(f'First array is: {arr1}\nSecond array is: {arr2}\nUnion of both array is: {res}')


# Changes