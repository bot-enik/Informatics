# https://informatics.msk.ru/mod/statements/view3.php?id=270&chapterid=226#1
# Task 226

n = int(input())
A = []
S = input().split()
for i in range(n):
  A += [int(S[i])]
k = int(input())

for i in range(len(A)):
    if A[i] == k:
        print(i+1, end=' ')
