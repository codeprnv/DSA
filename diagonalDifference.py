# Problem Statement: Given a square matrix, calculate the absolute difference between the sums of its diagonals. For example, the square matrix  is shown below:
# 1 2 3
# 4 5 6
# 9 8 9 
# The left-to-right diagonal = 1 + 5 + 9 = 15 .The right to left diagonal = 3 + 5 + 9 = 17 . Their absolute difference is | 15 - 17 | = 2.

def diagonalDifference(arr: list):
    print(arr) # Print the matrix
    #  Find the diagonals of the matrix(arr)
    d1 = [arr[i][i] for i in range(len(arr))]
    d2 = [arr[i][len(arr) - 1 - i] for i in range(len(arr))]
    
    # Calculate the sum of each diagonal respectively
    d1_sum, d2_sum = sum(d1), sum(d2)
    
    # Calculate the absolute difference between this diagonals
    result = abs(d1_sum - d2_sum)
    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]
res = diagonalDifference(matrix)
print(f'The absolute difference between diagonals of this matrix is: {res}')

# Changes