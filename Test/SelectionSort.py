def findMin(lis):

    temp = lis[0]
    for i in range(len(lis)):
        if temp < lis[i]:
            temp = lis[i]

        return temp

def Selectloop(lis):

    for i in range(len(lis)):
        temp = lis[i]
        for j in range(i,len(lis)):
            if lis[j] > lis[j+1]:
                temp = lis[i]