# https://informatics.msk.ru/mod/statements/view3.php?id=270&chapterid=1427#1
# Task 1427
# This solution is not fully correct

n, m = [int(i) for i in input().split()]
# n - число столбцов (x), m - число строк (y)
A = [[int(i) for i in input().split()] for j in range(m)]


res = 0
# Считаем строки
for B in A:
    min_B = min(B)
    c = B.count(min_B)
    # Ищем минимальные элементы в строке
    for i in range(n):
        if c == 0:
            break
        if B[i] == min_B:
            # Просмотрим этот столбец(проверка, что макс в нем)
            flag = True
            for j in range(m):
                if A[j][i] > B[i]:
                    flag = False
            if flag:
                res += 1
        c -= 1
print(res)
