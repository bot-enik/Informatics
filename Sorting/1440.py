# https://informatics.msk.ru/mod/statements/view3.php?id=270&chapterid=1440#1
# Task 1440

n = int(input())

maxn = 0
prev = 0
for i in input().split():
    a = int(i)
    if a > maxn:
        prev = maxn
        maxn = a
    elif a < maxn and a > prev:
        prev = a
print(prev)
