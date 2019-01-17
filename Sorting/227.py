# https://informatics.msk.ru/mod/statements/view3.php?id=270&chapterid=227#1
# Task 227

n = int(input())
A = []
S = input().split()
for i in range(n):
  A += [int(S[i])]

maxi = 0
for i in range(len(A)):
    if A[i] > A[maxi]:
        maxi = i
print(A[maxi])
