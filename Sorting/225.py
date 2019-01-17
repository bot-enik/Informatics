# https://informatics.msk.ru/mod/statements/view3.php?id=270&chapterid=225#1
# Task 225

n = int(input())
A = []
S = input().split()
for i in range(n):
  A += [int(S[i])]
k = int(input())

res = 0
diff = 65536
for i in A:
    d = abs(k - i)
    if d <= diff:
        diff = d
        res = i
print(res)
