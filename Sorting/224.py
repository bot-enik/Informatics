# https://informatics.msk.ru/mod/statements/view3.php?id=270&chapterid=224#1
# Task 224

n = int(input())

A = []
S = input().split()
for i in range(n):
  A += [int(S[i])]
# Вариант попроще, но без учета количества вводимых чисел:  
# A = [int(i) for i in input().split()]
  
k = int(input())


# Само решение:
for i in A:
    if i == k:
        print('YES')
        break
else:
    print('NO')

