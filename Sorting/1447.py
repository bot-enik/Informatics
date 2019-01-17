# https://informatics.msk.ru/mod/statements/view3.php?id=270&chapterid=1447#1
# Task 1447

A = [int(i) for i in input().split()]
n = A[0]
A.remove(A[0])

minn = min(A)
maxn = max(A)

for i in range(n):
    if A[i] == maxn:
        A[i] = minn
for i in A:
    print(i, end=' ')
