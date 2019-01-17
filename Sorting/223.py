# https://informatics.msk.ru/mod/statements/view.php?id=270#1
# Task 223

n = int(input())

A = []
S = input().split()
for i in range(n):
  A += [int(S[i])]
# Вариант попроще, но без учета количества вводимых чисел:  
# A = [int(i) for i in input().split()]
  
k = int(input())
count = 0

for i in A:
    if i == k:
        count += 1

print(count)
