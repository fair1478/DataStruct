def insertWithAscending(lis:list,val,index=0):

    if index >= len(lis) or lis==[]:
        return index

    if val > lis[index]:
       return insertWithAscending(lis,val,index+1)
    else:
        return index


def insertionSort(array:list,sub_arr:list=[]):

    if len(array) == 0:
        print("sorted")
        print(sub_arr)
        return 
    
    inn = insertWithAscending(sub_arr,array[0])

    temp = array.pop(0)

    sub_arr.insert(inn,temp)

    if len(sub_arr) != 1:
        print(f"insert {temp} at index {inn} :",sub_arr,end=' ')
        if len(array) != 0:
            print(array,end='')
        print()

    insertionSort(array,sub_arr)

    


inp = list(map(int,input("Enter Input : ").split()))

insertionSort(inp)







