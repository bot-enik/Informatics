# https://informatics.msk.ru/mod/statements/view3.php?id=270&chapterid=1427#1
# Task 1427
# This solution is not fully correct

# n - число строк (число списков)
# m - стобцов (элементов в одиночном списке)
n, m = [int(i) for i in input().split()]

A = [[int(i) for i in input().split()] for j in range(n)]


res = 0
# Считаем строки
for B in A:
    min_B = min(B)
    c = B.count(min_B)
    # Ищем минимальные элементы в строке
    for i in range(m):
        if c == 0:
            break
        if B[i] == min_B:
            # Просмотрим этот столбец(проверка, что макс в нем)
            for j in range(n):
                if A[j][i] > B[i]:
                    break
            else:
                res += 1
            c -= 1
print(res)
