import random
from Binary_search import Bin_search as binkS
from Simple_search import Simple_search as simS

n = 20
K = 0
N = [0]

# Генерируем случайный набор массивов
random.randint(0,3)

for i in range(10000):

    N = [0]
    for j in range(1,n):
        N += [N[j-1]+random.randint(0,3)]

    K = random.randint(0,10)
    
    bin_result = binkS(N, K, 0, n-1)
    simp_result = simS(N, K)

    if bin_result != simp_result:
        print('\n\n');
        print('There was an error, Testing data:')
        print('n = ', n)
        print('N = ', N)
        print('K = ', K)
        print('Binary method shows: ', bin_result)
        print('Simple method shows: ', simp_result)
        print('\n\n');
        print('Contunue? [Y/N]')
        ans = input();
        if ans == 'N':
            break
        
    if i % 100 == 0: 
        print ('Now we are at ', i, ' test')
