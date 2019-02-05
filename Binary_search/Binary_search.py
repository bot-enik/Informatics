# Binary search task A_2
# https://informatics.msk.ru/mod/statements/view.php?id=192

'''
n, k = [int(i) for i in input().split()]

N = [int(i) for i in input().split()]
K = [int(i) for i in input().split()]
'''

def Bin_search(Arr, numberToSearch, leftBoard, rightBoard):

    # Поиск элемента большего или равного искомому
    # (Если больше и таких чисел несколько, то число находящееся левее других)
    while leftBoard < rightBoard:
        middle = (leftBoard + rightBoard)//2
        if Arr[middle] == numberToSearch:
            break
        elif numberToSearch > Arr[middle]:
            leftBoard = middle + 1
        else:
            rightBoard = middle

    # Работа с краевыми случаями
    middle = (leftBoard + rightBoard)//2 ### Надо разкомментить

    if middle == 0:
        return Arr[0]
    if numberToSearch - Arr[middle-1] <= Arr[middle] - numberToSearch:
        return Arr[middle-1]
    else:
        return Arr[middle]

# Сама программа:
'''
for i in K:   
    print(Bin_search(N, i, 0, n-1))
'''

