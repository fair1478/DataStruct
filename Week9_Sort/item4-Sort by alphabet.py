def searchMaxIndex(array,j,i=0):

    if i == j:
        return i

    temp = searchMaxIndex(array,j,i+1)

    return i if array[i] > array[temp] else temp

def StraightSelectionSort(lis,index,order:list=[]):
    
    if index == 0 :
        return
    
    temp = searchMaxIndex(lis,index)

    if temp != index:
        order.append(temp)
        order.append(index)
        lis[temp], lis[index] = lis[index], lis[temp]

    StraightSelectionSort(lis,index-1,order)
    return order

def serchAlpha(st):

    temp = ''
    for i in st:
        if i.isalpha():
            temp = i
            break
    return temp


def Sortbyalphabet(lis):

    temp = []
    for i in lis:
        temp.append(ord(serchAlpha(i)))

    order = StraightSelectionSort(temp,len(temp)-1)
    for i in range(0,len(order),2):
        a = order[i]
        b = order[i+1]
        lis[a] , lis[b] =  lis[b] , lis[a]

    print(*lis)




lis = input("Enter Input : ").split()
Sortbyalphabet(lis)
