n = int(input('Enter the dimension: '))

# * * * *
# * * * *
# * * * *
# * * * * 

def pattern1(n):
    for i in range(n):
        for j in range(n):
            print('*', end = ' ')
        print()
        
pattern1(n)


# *
# * *
# * * *
# * * * *

def pattern2(n):
    for i in range(n + 1):
        for j in range(i):
            print('*', end= ' ')
        print()

pattern2(n)

# 1
# 1 2
# 1 2 3
# 1 2 3 4

def pattern3(n):
    for i in range(n + 1):
        for j in range(i):
            print(j + 1, end= ' ')
        print()

pattern3(n)

# 1
# 2 2
# 3 3 3
# 4 4 4 4

def pattern4(n):
    for i in range(n + 1):
        for j in range(i):
            print(i , end= ' ')
        print()

pattern4(n)

# * * * *
# * * *
# * *
# *

def pattern5(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print('*', end= ' ')
        print()

pattern5(n)

# 1 2 3 4 
# 1 2 3
# 1 2
# 1

def pattern6(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print(j+1, end=' ')
        print()

pattern6(n)

# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

def pattern7(n):
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

pattern7(n)


#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *

def pattern8(n):
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

pattern8(n)

# * * * * * * * * * 
#   * * * * * * *
#     * * * * *
#       * * *
#         *

def pattern9(n):
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

pattern9(n)

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

def pattern10(n):
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

pattern10(n)

# *   
# **  
# *** 
# ****
# *****
# ****
# *** 
# **  
# *

def pattern11(n):
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

pattern11(n)

# 1               1 
# 1 2           2 1
# 1 2 3       3 2 1
# 1 2 3 4   4 3 2 1

def pattern12(n):
    space = 2 * (n - 1)
    # Numbers
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        # Space
        for k in range(space + 1):
            print(' ',end=' ')
        for j in range(i, 0 , -1):
            print(j,end=' ')
        print()
        space -= 2    

pattern12(n)

# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

def pattern13(n):
    counter = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(counter, end=' ')
            counter += 1
        print()

pattern13(n)

# A
# A B
# A B C
# A B C D
# A B C D E

def pattern14(n):
    for i in range(n + 1):
        for j in range(i):
            print(chr(ord('A') + j),end=' ')
        print()

pattern14(n)

# A B C D E
# A B C D
# A B C
# A B
# A

def pattern15(n):
    counter = n
    for i in range(n + 1):
        for j in range(counter):
            print(chr(ord('A') + j), end=' ')
        counter -= 1
        print()

pattern15(n)

# A 
# B B
# C C C
# D D D D
# E E E E E

def pattern16(n):
    for i in range(n):
        for j in range(i + 1):
            print(chr(ord('A') + i),end=' ')
        print()

pattern16(n)

#         A
#       A B A
#     A B C B A
#   A B C D C B A
# A B C D E D C B A

def pattern17(n):
    for i in range(n):
        counter = 0
        peak = 2 * i + 1
        midpoint = peak // 2
        for k in range(n - i - 1):
            print(' ',end=' ')
        for j in range(peak):
            if(counter <= midpoint):
                ch = chr(ord('A') + counter) # ord() converts the string into integer ASCII value, chr() converts the integer ASCII value back to string
            else:
                ch = chr(ord('A') + (peak - counter - 1))
            print(ch, end=' ')
            counter += 1
        for k in range(n - i - 1):
            print(' ',end=' ')
        print()

pattern17(n)