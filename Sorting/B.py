# Task B
# https://informatics.mccme.ru/mod/statements/view3.php?id=271&chapterid=230
'''
n = int(input())
A = [int(i) for i in input().split()]


while n > 1:
    max_el = A[0]
    max_i = 0 
    for i in range(n):
        if A[i] > max_el:
            max_i = i
            max_el = A[i]
    A[max_i] = A[n-1]
    A[n-1] = max_el
    n -= 1

for i in A:
    print(i, end=" ")
'''

# Task C
# https://informatics.mccme.ru/mod/statements/view3.php?id=271&chapterid=231
'''
k = int(input())
A = [int(i) for i in input().split()]
n, ind = [int(i) for i in input().split()]

A = A[:ind-1] + [n] + A[ind-1:]
for i in A:
    print(i, end=" ")
'''

# Task D (----------)
# https://informatics.mccme.ru/mod/statements/view3.php?id=271&chapterid=232
'''
k = int(input())
A = [int(i) for i in input().split()]

def insert_with_shift(A, numb, ind):
    return A[:ind] + [numb] + A[ind:]

if A[0] > A[1]:
    B = [A[1], A[0]]
else:
    B = [A[0], A[1]]
    
ind = 0
for i in range(2,k):
    for j in range(len(B)):
        if B[j] >= A[i]:
            ind = j
            break 
    B = insert_with_shift(B, A[i], ind)

for i in B:
    print(i, end=" ")
'''

# Task E
# https://informatics.mccme.ru/mod/statements/view3.php?id=271&chapterid=233
'''
k = int(input())
A = [int(i) for i in input().split()]

for i in range(k):
    for j in range(k-i-1):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
    
for i in A:
    print(i, end=" ")
'''

# Task F (----------)
k = int(input())
A = [int(i) for i in input().split()] 

def find_max_ind(A):
    ind = 0
    for i in range(len(A)):
        if A[i] > A[ind]:
            ind = i
    return ind

m = 0
n = 0

for i in A:
    ind = find_max_ind(A[:k-m])
    n += (k - (ind+1) - m)
    m += 1

print(n)

# Task I
# https://informatics.mccme.ru/mod/statements/view3.php?id=271&chapterid=1446#1
'''
n = int(input())
B = []
A = []
for i in range(n):
    key, val = [int(i) for i in input().split()]
    B += [key]
    A += [val]

k = len(A)
for i in range(k):
    for j in range(k-i-1):
        if A[j] < A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
            B[j], B[j+1] = B[j+1], B[j]


for i in range(k):
    for j in range(k-i-1):
        if A[j] == A[j+1]:
            if B[j] > B[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                B[j], B[j+1] = B[j+1], B[j]        

for i in range(k):
    print(B[i], A[i])

'''       






