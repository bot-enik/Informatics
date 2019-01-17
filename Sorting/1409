# https://informatics.msk.ru/mod/statements/view3.php?id=270&chapterid=1409#1
# Task 1409

n = int(input())
A = []
S = input().split()
for i in range(n):
  A += [int(S[i])]

minim = A[0]
pr_min = A[1]

for i in A:
    if i < minim:
        pr_min = minim
        minim = i
    elif i > minim and i < pr_min:
        pr_min = i
print(minim, pr_min)
