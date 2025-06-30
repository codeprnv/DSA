# Find the intersection of two arrays arr1 and arr2 of length n and m respectively

def intersection(arr1, arr2):
    # Find the length of the both arrays
    n = len(arr1)
    m = len(arr2)
    # Initialize two pointers with 0 i.e first element in the array
    i = 0
    j = 0
    # Initialize a empty array intersection that will contain similar elements from both the arrays
    intersection_arr = []
    # Iterate over both the arrays while the pointers are less than the length of the arrays
    while(i < n and j < m):
        if(arr1[i] == arr2[j]):
            intersection_arr.append(arr1[i])
            i += 1
            j += 1
        elif(arr1[i] < arr2[j]):
            i += 1
        else:
            j += 1
    return intersection_arr

arr1 = [1,2,3,3,4,5,6,7,8,9,10]
arr2 = [2,3,3,4,4,5,11,12]

res = intersection(arr1, arr2)
print(f'First array is: {arr1}\nSecond array is: {arr2}\nIntersection of both array is: {res}')