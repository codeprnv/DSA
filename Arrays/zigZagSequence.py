# Zig Zag Sequence

def findZigZagSequence(a, n):
    a.sort()
    mid = int(n / 2)
    a[mid], a[n - 1] = a[n - 1], a[mid]
    
    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st += 1
        ed -= 1
        
    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return

a = [82, 12, 14, 20, 74, 34, 76, 69]
print(f'Array is: {a}')
n = len(a)
findZigZagSequence(a, n)