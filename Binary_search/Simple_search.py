
'''
n, k = [int(i) for i in input().split()]

N = [int(i) for i in input().split()]
K = [int(i) for i in input().split()]
'''


def Simple_search(Arr, search):
    i = 0
    for j in Arr:
        if j >= search:
            break
        i += 1
        
    if i == 0:
        return Arr[0]
    elif search - Arr[i-1] <= Arr[i] - search:
        i -= 1
    
    return Arr[i]

# Сама программа
'''
for i in K:
    print(Simple_search(N, i))
'''

