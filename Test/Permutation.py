
def ascending(ls,index):
    if index<=0:
        return
    if ls[index] < ls[index-1]:
        ls[index],ls[index-1] = ls[index-1],ls[index]
    ascending(ls,index-1)

    if ls[index] < ls[index-1]:
        ls[index],ls[index-1] = ls[index-1],ls[index]
    ascending(ls,index-1)

lis = [5,4,3,6,2,1]
ascending(lis,len(lis)-1)
print(lis)