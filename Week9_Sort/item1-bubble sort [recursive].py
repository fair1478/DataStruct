def bubbleSort(n:int,lis:list):

    if n < 0:
        return
    
    bubbleSort(n-1,lis)
    if lis[n] > lis[n+1]:
        lis[n] , lis[n+1] = lis[n+1] , lis[n]

    
    bubbleSort(n-1,lis)
    if lis[n] > lis[n+1]:
        lis[n] , lis[n+1] = lis[n+1] , lis[n]

    return lis
    


lis = [] or list(map(int,input("Enter Input : ").split()))
print(bubbleSort(len(lis)-2,lis))


'''
def mergeSort(l,left,right)
    center = (left + right) // 2
    if left < right:
        mergeSort(l,left,center)
        mergeSort(l,center+1,right)
    merge(l,left,center,center+1,right)


def merge()

'''