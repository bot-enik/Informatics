# https://informatics.msk.ru/mod/statements/view3.php?id=270&chapterid=1412
# Task 1412

x = int(input())
n = int(input())
A = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    B = input().split()
    for j in range(n):
        A[i][j] = int(B[j])

for i in range(n):
    for j in range(n):
        if A[j][i] == x:
            print('YES')
            break
    else:
        print('NO')
    
