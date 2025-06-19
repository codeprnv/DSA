n = int(input('Enter the dimension: '))

# * * * *
# * * * *
# * * * *
# * * * * 

for i in range(n):
    for j in range(n):
        print('*', end = ' ')
    print(' ')


# *
# * *
# * * *
# * * * *

for i in range(n + 1):
    for j in range(i):
        print('*', end= ' ')
    print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4

for i in range(n + 1):
    for j in range(i):
        print(j + 1, end= ' ')
    print()

# 1
# 2 2
# 3 3 3
# 4 4 4 4

for i in range(n + 1):
    for j in range(i):
        print(i , end= ' ')
    print()

# * * * *
# * * *
# * *
# *

for i in range(n, 0, -1):
    for j in range(i):
        print('*', end= ' ')
    print()

# 1 2 3 4 
# 1 2 3
# 1 2
# 1

for i in range(n, 0, -1):
    for j in range(i):
        print(j+1, end=' ')
    print()

# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

for i in range(n):
    start = 1
    if(i % 2 == 0):
        start = 1
    else:
        start = 0
    for j in range(i+1):
        print(start, end=' ')
        start = 1 - start
    print()


#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *

for i in range(n):
        # Space
        for k in range(n - i - 1, 0 , -1):
            print(' ',end='')
        # Star
        for j in range(0, 2 * i + 1 ,1):
            print('*',end='')
        # Space
        for k in range(n - i - 1, 0, -1):
            print(' ',end='')
        print()

# * * * * * * * * * 
#   * * * * * * *
#     * * * * *
#       * * *
#         *

for i in range(n):
    # Space
    for k in range(i):
        print(' ',end=' ')
    # Star
    for j in range(2 * n - (2 * i + 1)):
        print('*', end=' ')
    # Space
    for k in range(i):
        print(' ',end=' ')
    print()

#     *    
#    ***   
#   *****  
#  ******* 
# *********
# *********
#  ******* 
#   *****  
#    ***   
#     *  

def equilateral_reverseEquilateral_triangle(n):
    for i in range(n):
        # Space
        for k in range(n - i - 1, 0, -1):
            print(' ',end='')
        # Stars
        for j in range(2 * i + 1):
            print('*',end='')
        # Space
        for k in range(n - i - 1, 0, -1):
            print(' ',end='')
        print()

    for i in range(n):
        # Space
        for k in range(i):
            print(' ',end='')
        # Star
        for j in range(2 * n - (2 * i + 1)):
            print('*', end='')
        # Space
        for k in range(i):
            print(' ',end='')
        print()

equilateral_reverseEquilateral_triangle(n)

# *   
# **  
# *** 
# ****
# *****
# ****
# *** 
# **  
# *

for i in range(n):
    for j in range(i):
        print('*',end='')
    for k in range(n - i - 1, 0, -1):
        print(' ',end='')
    print()

for i in range(n, 0, -1):
    for j in range(i):
        print('*',end='')
    for k in range(n - i - 1):
        print(' ',end='')
    print()