
def merge_sort(array):
    L = len(array)
    if L == 1:
        return array
    else:
        part1 = merge_sort(array[0:L//2])
        part2 = merge_sort(array[L//2:])
        l1 = len(part1)
        l2 = len(part2)
        i1 = 0
        i2 = 0
        arrayToReturn = [0]*(l1 + l2)
        for i in range(l1 + l2):
            if  i1 >= l1:
                arrayToReturn[i] = part2[i2]
                i2 += 1
            elif i2 >= l2:
                arrayToReturn[i] = part1[i1]
                i1 += 1
            else:
                if part1[i1] <= part2[i2]:
                    arrayToReturn[i] = part1[i1]
                    i1 += 1
                else:
                    arrayToReturn[i] = part2[i2]
                    i2 += 1
            #print (f'arrayToReturn = {arrayToReturn}')
        return arrayToReturn

def main():

    n = int(input())
    A = [int(i) for i in input().split()]
    print(" ".join([str(i) for i in merge_sort(A)]))



if __name__ == "__main__":
    main()
