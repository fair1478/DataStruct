def searchMaxIndex(array,j,i=0):

    if i == j:
        return i

    temp = searchMaxIndex(array,j,i+1)

    return i if array[i] > array[temp] else temp

def StraightSelectionSort(lis,index):
    
    if index == 0 :
        return
    
    temp = searchMaxIndex(lis,index)

    if temp != index:
    
        lis[temp], lis[index] = lis[index], lis[temp]
        print(f"swap {lis[temp]} <-> {lis[index]} :",lis)

    StraightSelectionSort(lis,index-1)

lis = list(map(int,input("Enter Input : ").split()))

StraightSelectionSort(lis,len(lis)-1)

print(lis)
